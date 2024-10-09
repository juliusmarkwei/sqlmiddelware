# SQLMiddleware Project: Product API

This project is a Django-based application that provides a RESTful API for managing products. The main purpose of this project is to understand how django middleware works.

## Features

- Retrieve all products in JSON format.
- The API is built using Django's built-in serialization and JSONResponse for easy data exchange.
- Build and implement a custom middleware in django

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:
```
git clone https://github.com/juliusmarkwei/sqlmiddleware.git
```

2. Navigate to the project directory:
```
cd sqlmiddleware
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Run the Django development server:
```
python manage.py runserver
```

5. Access the API at http://localhost:8000/api/products/

## API Endpoints

The following API endpoint is available in this project:

- `GET /api/products/`: Retrieves all products in JSON format.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.