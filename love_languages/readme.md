
**Love Language README**

**Overview:**
This Python script is designed to simulate a test for identifying a person's primary love language, which can help understand how they express and receive love in a relationship. The script uses a simplified model with five love languages: "words," "acts," "gifts," "time," and "touch."

**Code Components:**

1. **`love_language(partner, weeks)` Function:**
   - This function takes two parameters:
     - `partner`: An instance of the `TestPartner` class, which simulates a partner with a specific primary love language.
     - `weeks`: The number of weeks over which the simulation runs.
   - Inside the function, it initializes a dictionary `response_counts` to keep track of positive responses for each love language.
   - It then iterates through each love language for each day in the specified number of weeks, simulating a partner's responses.
   - The function calculates and returns the primary love language based on the highest count of positive responses.

2. **`TestPartner` Class:**
   - This class represents a partner and is used to simulate their responses to different love languages.
   - The `__init__` method takes the partner's primary love language as an argument.
   - The `response` method simulates the partner's response to a given love language, taking into account their primary love language. It returns either "positive" or "neutral" based on a random probability.

3. **`run_tests()` Function:**
   - This function is responsible for running tests to validate the `love_language` function.
   - It sets the number of weeks to 6 and creates instances of the `TestPartner` class with different primary love languages.
   - It then calls the `love_language` function for each partner and prints the test results, asserting that the results match the expected primary love languages.

**How to Use:**

1. To use this script for your own tests or simulations, you can create instances of the `TestPartner` class with different primary love languages and call the `love_language` function with those partners.

2. Modify the number of weeks in the `run_tests()` function to change the duration of the simulation.

3. The script includes assertions to verify that the primary love language identified by the `love_language` function matches the expected result for each test case.

4. You can extend or modify the code as needed to suit your specific requirements for simulating love language tests.

5. Ensure that you have Python installed, and you can run the script by executing it in your Python environment.
