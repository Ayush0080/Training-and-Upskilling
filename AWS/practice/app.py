from flask import Flask, request, render_template_string, redirect
import psycopg2

app = Flask(__name__)

# 🔹 Replace with your RDS info
DB_HOST = "*"
DB_NAME = "*"
DB_USER = "*"
DB_PASS = "*"

# 🔹 HTML Template with Bootstrap
HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Employee Portal</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-5">
  <h1 class="text-center mb-4">Employee Portal</h1>

  <!-- Add Employee -->
  <div class="card shadow-sm p-4 mb-4">
    <h3>Add Employee</h3>
    <form method="POST" action="/add">
      <div class="row">
        <div class="col-md-4">
          <input type="text" class="form-control" name="name" placeholder="Name" required>
        </div>
        <div class="col-md-4">
          <input type="text" class="form-control" name="department" placeholder="Department" required>
        </div>
        <div class="col-md-3">
          <input type="number" class="form-control" name="salary" placeholder="Salary" required>
        </div>
        <div class="col-md-1">
          <button type="submit" class="btn btn-primary w-100">Add</button>
        </div>
      </div>
    </form>
  </div>

  <!-- Search Employee -->
  <div class="card shadow-sm p-4 mb-4">
    <h3>Search Employee</h3>
    <form method="GET" action="/search">
      <div class="row">
        <div class="col-md-10">
          <input type="text" class="form-control" name="name" placeholder="Enter employee name" required>
        </div>
        <div class="col-md-2">
          <button type="submit" class="btn btn-success w-100">Search</button>
        </div>
      </div>
    </form>
  </div>

  <!-- Employee Details (only after search) -->
  {% if employee %}
  <div class="card shadow-sm p-4 mt-4 border-success">
    <h3>Employee Details</h3>
    <p><strong>ID:</strong> {{ employee[0] }}</p>
    <p><strong>Name:</strong> {{ employee[1] }}</p>
    <p><strong>Department:</strong> {{ employee[2] }}</p>
    <p><strong>Salary:</strong> ₹{{ employee[3] }}</p>
    <a href="/delete/{{ employee[0] }}" class="btn btn-danger" onclick="return confirm('Delete this employee?')">Delete</a>
  </div>
  {% elif searched %}
  <div class="alert alert-warning mt-3">No employee found with that name.</div>
  {% endif %}

</div>
</body>
</html>
"""

# ---------- DB CONNECTION ----------
def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

# ---------- ROUTES ----------
@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML, employee=None, searched=False)

@app.route("/add", methods=["POST"])
def add_employee():
    name = request.form["name"]
    department = request.form["department"]
    salary = request.form["salary"]

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s);",
                (name, department, salary))
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/")

@app.route("/search", methods=["GET"])
def search_employee():
    name = request.args.get("name")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees WHERE name ILIKE %s;", (name,))
    employee = cur.fetchone()
    cur.close()
    conn.close()
    return render_template_string(HTML, employee=employee, searched=True)

@app.route("/delete/<int:id>", methods=["GET"])
def delete_employee(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id = %s;", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/")

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
