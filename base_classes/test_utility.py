class OutputConsoleResult:
    @staticmethod
    def print_result(result):
        """
        Prints IP addresses. If the list is shorter than 50, print all.
        Otherwise, print the first 50 with ellipsis.
        """
        result = str(result)
        if len(result) < 50:
            print(f"Result: {result}")
        else:
            print(f"Result: {result[:50]}...")
