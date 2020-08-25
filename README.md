## Appium User Journey 

This test case follows the user joiurney scoped out for the Wayfair/Headspin POC. Simple user journey of navigation to a given product and selecting that product. The Test case will execute on both devices in the Wayfair org (1 iOS and 1 Android)

### Running the Test Suite

Note: Requires Python 2.7.17 to be installed on your system

To run the test case your will also need to grab your API token from the Headspin UI. You will pass this API token as an enviormental variable in the launch command. 

```

pip install -r requirements.txt
HS_API_TOKEN={Your-API-Token} pytest -s --disable-warnings
```

### Structure

This test suite foolows the Page Object Pattern for test cases. In the tests directory you will find the initalization of each driver for the respective devices and the corresponding user journey. The page directory contains the objects pertaining the the selectors and action on UI elements. To change the target device you will want to edit the `conftest.py` file under the test directory whihc contains the webdriver URL and capabilities. 