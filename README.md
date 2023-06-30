# ShadStore

This is an electronic book store with a unique twist.

## Functionality

ShadStore offers a range of features to enhance your book shopping experience:

1. **Extensive Book Collection**: Our platform boasts a vast collection of books across various genres, ensuring you can find your favorite titles or discover new ones easily.

2. **Intuitive Search**: Find books quickly using our advanced search engine that allows filtering by author, title, genre, or keywords.

3. **Personalized Recommendations**: Benefit from machine learning algorithms that provide personalized book recommendations based on your preferences and reading history.

4. **User Reviews and Ratings**: Make informed decisions with insightful reviews and ratings from fellow book enthusiasts.

5. **Seamless Checkout Process**: Enjoy a smooth and secure transaction experience, with options to add books to your cart, apply discounts, and choose from multiple payment methods.

## Development Modes

ShadStore operates in two modes: **Development Mode** and **Server Mode**.

1. **Development Mode**: This is the default mode for local development. It allows developers to test and refine features without external dependencies.

2. **Server Mode (Dockerized)**: The Server Mode enables production deployment using Docker containers. It offers scalability, reliability, and easy maintenance through containerization.

## How to run

#### Developer Mode 
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### Server Mode
```bash
docker-comose build
docker-comose up
```

### Home page
<img src="/static/image/home.png" alt="home" title="Home Page" style='text-align: center;'>

### About page
<img src="/static/image/about.png" alt="home" title="Home Page" style='text-align: center;'>

### Login page
<img src="/static/image/login.png" alt="home" title="Home Page" style='text-align: center;'>

### Book Collection page
<img src="/static/image/books.png" alt="home" title="Home Page" style='text-align: center;'>

### Book Detail page
<img src="/static/image/book-detail.png" alt="home" title="Home Page" style='text-align: center;'>
