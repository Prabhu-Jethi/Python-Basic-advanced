'''Exception Handling is a mechanism used to manage errors that occur during the execution of a program (runtime errors). 
Instead of letting the application crash, exception handling allows the program to catch the error, deal with it gracefully, and continue running.'''


def safe_divide(numerator, denominator):
    try:
        # Code that might crash (e.g., if denominator is 0 or a string)
        result = numerator / denominator
    except ZeroDivisionError:
        # Handles division by zero
        return "Error: Cannot divide by zero!"
    except TypeError:
        # Handles mixing incompatible data types (e.g., integer and string)
        return "Error: Both inputs must be numbers!"
    else:
        # Runs only if the try block succeeded without crashing
        print("Division completed successfully.")
        return result
    finally:
        # Always runs, no matter what (even if a return statement was hit)
        print("Execution of safe_divide is complete.\n")

# --- Test Cases ---
print(safe_divide(10, 2))  # Case 1: Succeeds (Triggers else & finally)
print(safe_divide(10, 0))  # Case 2: ZeroDivisionError (Triggers except & finally)
print(safe_divide(10, "2")) # Case 3: TypeError (Triggers except & finally)
