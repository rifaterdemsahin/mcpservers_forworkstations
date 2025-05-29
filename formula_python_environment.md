To set up a Python virtual environment and install the necessary libraries for your email script, follow these steps:

### 1. Set Up a Virtual Environment

1. **Navigate to Your Project Directory**:
   Open your terminal and change the directory to your project's root folder.

   ```shell
   cd /path/to/your/project
   ```

2. **Create a Virtual Environment**:

   ```shell
   python -m venv env
   python3 -m venv env
   ```

   This will create a new directory named `env` in your project directory, containing the virtual environment files.

3. **Activate the Virtual Environment**:
   - **On Windows**:

     ```shell
     .\env\Scripts\activate
     ```

   - **On macOS and Linux**:

     ```shell
     source env/bin/activate
     ```

### 2. Install Required Libraries

Once your virtual environment is activated, you can install the required Python libraries:

1. **Install Libraries with Pip**:

   ```shell
   pip install smtplib email mime python-dotenv
   ```

   Note: `smtplib` and `email` are part of Python's standard library, so this step effectively ensures you have `python-dotenv`.

### 3. Final Step: Run Your Script

1. **Ensure Your `.env` File is Set Up**:
   Make sure your `.env` file is in the same directory as your Python script and contains your SMTP server credentials.

2. **Run Your Script**:
   Execute your Python script with the following command:

   ```shell
   python symbols_email_sender.py
   ```

By following these steps, you should be able to set up your virtual environment and run your script successfully. Make sure to deactivate the virtual environment when you're done:

```shell
deactivate
```

This will return you to your system's default Python interpreter. If you need further assistance with executing these steps, feel free to ask!