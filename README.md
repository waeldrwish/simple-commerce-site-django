# Simple E-commerce Product Listing Page

This project is a basic e-commerce product listing webpage built using Python and Django. It showcases a variety of products along with their images, names, and prices. The webpage offers a user-friendly interface to view and explore the available products.

## Getting Started

To run this project locally, follow these steps:

1. **Clone the Repository:**
Replace `<repository-url>` with the actual URL of your repository.
git clone <repository-url>

2. **Navigate to the Project Directory:**
cd project-directory
Replace `project-directory` with the name of the directory where you cloned the repository.

3. **Install Dependencies:**
Create and activate a virtual environment (recommended) and then install the required packages:
pip install -r requirements.txt

4. **Apply Migrations:**
Apply database migrations to set up the database schema:
python manage.py migrate

5. **Create Admin User:**
Create an admin user by running the following command and following the prompts:
python manage.py createsuperuser

6. **Run the Development Server:**
Start the development server:
python manage.py runserver
The webpage will be accessible at `http://127.0.0.1:8000/` by default.

7. **Explore the Webpage:**
Open a web browser and navigate to `http://127.0.0.1:8000/` to explore the e-commerce product listing page.

8. **Access Admin Panel:**
To access the admin panel, go to `http://127.0.0.1:8000/admin/` and log in with the admin credentials you created in step 5.

## Additional Notes

- This project uses Django's built-in development server. For a production environment, consider using a production-ready server like Gunicorn or uWSGI.
- Remember to replace `<repository-url>` with the actual URL of your repository in step 1.

Feel free to customize and enhance the project according to your requirements. Happy coding!
