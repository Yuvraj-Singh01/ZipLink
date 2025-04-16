# ZipLink

ZipLink is a simple and fast link shortening service that allows users to shorten URLs and generate QR codes for easy sharing. This project is built using Django and provides a user-friendly interface for managing links and QR codes.

## Features

-   **URL Shortening**: Convert long URLs into short, shareable links.

-   **QR Code Generation**: Generate QR codes for any URL.

-   **User Authentication**: Secure login and logout functionality.

-   **Responsive Design**: Optimized for both desktop and mobile devices.

## Technologies Used

-   **Backend**: Django (Python)

-   **Frontend**: HTML, CSS (with custom styles)

-   **Database**: SQLite

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd ZipLink
    ```

2. Create a virtual environment and activate it:

    - On macOS/Linux:
        ```bash
        python -m venv venv
        source venv/bin/activate
        ```
    - On Windows:
        ```cmd
        python -m venv venv
        venv\Scripts\activate
        ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

-   **Shorten a URL**: Enter a URL on the homepage and click the "Shorten" button to generate a short link.

-   **Generate a QR Code**: Navigate to the QR Code page, enter a URL, and click "Generate QR" to create a QR code.

-   **User Authentication**: Log in to access personalized features.

## Project Structure

-   `base/`: Contains the core app files (models, views, URLs, etc.).

-   `templates/`: HTML templates for the frontend.

-   `static/`: Static files such as CSS and images.

-   `media/`: Directory for storing generated QR code images.

-   `ZipLink/`: Project-level settings and configurations.

## Contributing

Contributions are welcome! To contribute to this project, follow these steps:

1. **Fork the Repository**: Click the "Fork" button on the repository's GitHub page to create a copy of the repository in your GitHub account.

2. **Clone the Forked Repository**: Clone the forked repository to your local machine:

    ```bash
    git clone <your-forked-repository-url>
    cd ZipLink
    ```

3. **Create a New Branch**: Create a new branch for your feature or bug fix:

    ```bash
    git checkout -b feature-or-bugfix-name
    ```

4. **Make Changes**: Implement your changes in the codebase. Ensure your code follows the project's coding standards and conventions.

5. **Test Your Changes**: Run the project locally and test your changes to ensure they work as expected:

    ```bash
    python manage.py runserver
    ```

6. **Commit Your Changes**: Commit your changes with a descriptive commit message:

    ```bash
    git add .
    git commit -m "Description of the changes made"
    ```

7. **Push to Your Fork**: Push your changes to your forked repository:

    ```bash
    git push origin feature-or-bugfix-name
    ```

8. **Submit a Pull Request**: Go to the original repository on GitHub and submit a pull request. Provide a clear and detailed description of your changes in the pull request.

9. **Address Feedback**: Be responsive to any feedback or requested changes from the project maintainers.

Thank you for contributing!

## Contributors

We extend our gratitude to the following individuals for their contributions to the project:

-   **Yuvraj Singh**: https://github.com/Yuvraj-Singh01

-   **Deepali**: https://github.com/lavenderpeaches

If you would like to contribute, please refer to the [Contributing](#contributing) section above.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries or feedback, please contact yuvsingh18@gmail.com or deepalix7@gmail.com.