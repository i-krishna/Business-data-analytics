-- Change Request: Add 'ReportType' column to 'Sales' table
-- Author: Krishna
-- Date: 2025-08-22

BEGIN TRANSACTION;

ALTER TABLE Sales
ADD ReportType VARCHAR(50) NULL;

-- Optional: Backfill data
-- UPDATE Sales SET ReportType = 'Standard' WHERE ReportType IS NULL;

COMMIT TRANSACTION;
-- Document change in schema log and version control
