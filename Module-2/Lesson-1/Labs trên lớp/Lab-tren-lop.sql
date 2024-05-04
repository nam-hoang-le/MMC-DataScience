-- Active: 1714793884232@@127.0.0.1@3306
CREATE DATABASE Module2_Lab1;

USE Module2_Lab1;

CREATE TABLE Customers (
    customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, # auto insert when new values are added 
    first_name VARCHAR(255) NOT NULL, last_name VARCHAR(255) NOT NULL, email_address VARCHAR(255) NOT NULL, number_of_complaints INT NOT NULL
)

CREATE TABLE Items (
    item_code VARCHAR(255) NOT NULL PRIMARY KEY, item VARCHAR(255) NOT NULL, unit_price_usd INT NOT NULL, company VARCHAR(255) NOT NULL, headquarters_phone_number VARCHAR(255) NOT NULL
)

CREATE TABLE SALES (
    purchase_number INT NOT NULL AUTO_INCREMENT PRIMARY KEY, date_of_purchase DATE NOT NULL, customer_id INT NOT NULL, item_code VARCHAR(255) NOT NULL, FOREIGN KEY (customer_id) REFERENCES Customers (customer_id), FOREIGN KEY (item_code) REFERENCES Items (item_code)
)