-- Ensure proper permissions
SET GLOBAL local_infile = 1;

-- Create database
CREATE DATABASE IF NOT EXISTS ggulgguk 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_general_ci;

USE ggulgguk;

-- Force table creation
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  username VARCHAR(100) NOT NULL,
  hashed_password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE INDEX email_unique (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Add test data
INSERT INTO users (email, username, hashed_password) 
VALUES ('test@example.com', 'testuser', 'placeholder_hash');

-- Verify creation
SELECT 'USERS TABLE CREATED' AS confirmation;
