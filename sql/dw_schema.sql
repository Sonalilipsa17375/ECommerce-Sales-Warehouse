-- Create Categories Table
CREATE TABLE categories (
    CategoryId INT PRIMARY KEY, -- IDs are provided in the CSV
    categories VARCHAR(255) NOT NULL -- Column name 'categories' matches the CSV
);

-- Create Products Table
CREATE TABLE products (
    ProductsId INT PRIMARY KEY, -- IDs are provided in the CSV
    title VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    description TEXT,
    CategoryId INT REFERENCES Categories(CategoryId),
    image VARCHAR(255),
    rate FLOAT,
    count INT
);

-- Create Address Table
CREATE TABLE address (
    AddressId INT PRIMARY KEY, -- IDs are provided in the CSV
    city VARCHAR(255),
    street VARCHAR(255),
    number INT,
    zipcode VARCHAR(255),
    latitude FLOAT,
    longitude FLOAT
);

-- Create Users Table
CREATE TABLE users (
    UsersId INT PRIMARY KEY, -- IDs are provided in the CSV
    email VARCHAR(255) NOT NULL,
    username VARCHAR(255),
    password VARCHAR(255),
    phone VARCHAR(255),
    AddressId INT REFERENCES Address(AddressId),
    firstname VARCHAR(255),
    lastname VARCHAR(255)
);

-- Create Carts Table
CREATE TABLE carts (
    CartsId INT PRIMARY KEY, -- IDs are provided in the CSV
    userId INT REFERENCES Users(UsersId),
    date DATE NOT NULL,
    productId INT REFERENCES Products(ProductsId),
    quantity INT NOT NULL,
    test INT
);