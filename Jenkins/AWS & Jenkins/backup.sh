#!/bin/bash

set -e

DATE=$(date +"%Y-%m-%d_%H-%M-%S")
DB_USER="root"
DB_PASS="root123"
DB_NAME="appdb"
CONTAINER="mysql-db"
BACKUP_DIR="/opt/mysql-backup-project/backups"
S3_BUCKET="s3://my-mysql-backups-bucket-0080 " 

mkdir -p $BACKUP_DIR

echo "[INFO] Taking MySQL backup from container $CONTAINER..."
docker exec $CONTAINER mysqldump -u$DB_USER -p$DB_PASS $DB_NAME > $BACKUP_DIR/$DB_NAME-$DATE.sql

echo "[INFO] Compressing backup..."
gzip $BACKUP_DIR/$DB_NAME-$DATE.sql

BACKUP_FILE="$BACKUP_DIR/$DB_NAME-$DATE.sql.gz"

echo "[INFO] Uploading backup file: $BACKUP_FILE"
echo "[INFO] Uploading to bucket: $S3_BUCKET"

aws s3 cp "$BACKUP_FILE" "$S3_BUCKET" --only-show-errors

echo "[SUCCESS] Backup Completed at $(date)"