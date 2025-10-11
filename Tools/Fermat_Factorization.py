import gmpy2
import math
from gmpy2 import mpz, isqrt, is_square, sub, add
import sys, time, itertools

def fermat_factorization(n, max_iterations=100000):
    """
    Fermat Factorization Algorithm
    
    Args:
        n: Number to factorize (mpz integer)
        max_iterations: Maximum number of iterations to try
    
    Returns:
        Tuple (p, q) if factors found, None otherwise
    """
    # Convert to mpz if not already
    n = mpz(n)
    
    # Check if n is even
    if n % 2 == 0:
        return mpz(2), n // 2
    
    # Check if n is a perfect square
    root = isqrt(n)
    if root * root == n:
        return root, root
    
    # Fermat's method
    x = isqrt(n) + 1
    iterations = 0
    
    while iterations < max_iterations:
        x_squared = x * x
        y_squared = x_squared - n
        
        # Check if y_squared is a perfect square
        if y_squared >= 0:
            y = isqrt(y_squared)
            
            if y * y == y_squared:
                # Found factors: n = (x - y) * (x + y)
                p = x - y
                q = x + y
                
                # Verify the factorization
                if p * q == n:
                    return p, q
        
        x += 1
        iterations += 1
    
    return None

def fermat_factorization_optimized(n, max_iterations=100000):
    """
    Optimized Fermat Factorization with better performance
    
    Args:
        n: Number to factorize (mpz integer)
        max_iterations: Maximum number of iterations to try
    
    Returns:
        Tuple (p, q) if factors found, None otherwise
    """
    n = mpz(n)
    
    # Check small factors first
    if n % 2 == 0:
        return mpz(2), n // 2
    
    # Check for perfect square
    root = isqrt(n)
    if root * root == n:
        return root, root
    
    # Optimized: Start from ceiling(sqrt(n))
    x = isqrt(n)
    if x * x < n:
        x += 1
    
    iterations = 0
    
    while iterations < max_iterations:
        # Calculate x^2 - n
        x_squared = x * x
        y_squared = x_squared - n
        
        if y_squared < 0:
            x += 1
            iterations += 1
            continue
        
        y = isqrt(y_squared)
        
        # Check if perfect square
        if y * y == y_squared:
            p = x - y
            q = x + y
            
            if p * q == n:
                return p, q
        
        x += 1
        iterations += 1
    
    return None

def fermat_factorization_with_stats(n, max_iterations=100000):
    """
    Fermat Factorization with progress statistics
    
    Args:
        n: Number to factorize (mpz integer)
        max_iterations: Maximum number of iterations to try
    
    Returns:
        Dictionary with factors and statistics
    """
    n = mpz(n)
    start_x = isqrt(n)
    if start_x * start_x < n:
        start_x += 1
    
    iterations = 0
    x = start_x
    
    while iterations < max_iterations:
        x_squared = x * x
        y_squared = x_squared - n
        
        if y_squared >= 0:
            y = isqrt(y_squared)
            
            if y * y == y_squared:
                p = x - y
                q = x + y
                
                if p * q == n:
                    return {
                        'factors': (p, q),
                        'iterations': iterations,
                        'start_x': start_x,
                        'final_x': x,
                        'distance': x - start_x,
                        'success': True
                    }
        
        x += 1
        iterations += 1
        spinner = itertools.cycle(['|', '/', '-', '\\'])
        # Print progress every 10000 iterations
        if iterations % 10000 == 0:
            print(f"Iteration {iterations}, current x: {x}")
            sys.stdout.write(f"\rWorking {next(spinner)}  Iteration {iterations:,}")
            sys.stdout.flush()
            time.sleep(0.05)
    
    return {
        'factors': None,
        'iterations': iterations,
        'start_x': start_x,
        'final_x': x,
        'distance': x - start_x,
        'success': False
    }
def print_rsa_components(n,p,q):
    """
    Display RSA key components clearly in the terminal.
    Includes verification that n = p × q.
    """

    verification = (n == p * q)

    print("\n" + "=" * 60)
    print("🔐  RSA KEY COMPONENTS".center(60))
    print("=" * 60)
    print(f"p (prime 1) : {p} ,")
    print(f"q (prime 2) : {q} ,")
    print("-" * 60)
    print(f"n = p × q   : {n} ,")
    print(f"n (hex)     : {hex(n)}")
    print(f"n bit length: {n.bit_length()} bits")
    print("-" * 60)

    # ✅ Verification Section
    if verification:
        print("✅ Verification: n equals p × q ✔️")
    else:
        print("❌ Verification FAILED: n ≠ p × q ⚠️")

    print("=" * 60 + "\n")




def get_user_input():
    """
    Get and validate user input for factorization
    """
    print("Fermat Factorization Tool")
    print("=" * 40)
    
    while True:
        try:
            n_input = input("\nEnter the number to factorize (or 'quit' to exit): ").strip()
            
            if n_input.lower() == 'quit':
                return None
            
            # Convert to mpz for large number support
            n = mpz(n_input)
            
            if n <= 1:
                print("Please enter a number greater than 1.")
                continue
                
            return n
            
        except KeyboardInterrupt:
            print("\n\nExiting program. Goodbye!")
            return None
        except Exception as e:
            print(f"Invalid input: {e}. Please enter a valid integer.")

def main():
    """
    Main function with user interaction
    """
    print("Fermat Factorization using gmpy2")
    print("This tool is useful for RSA factorization when primes are close together")
    print("=" * 60)
    
    while True:
        n = get_user_input()
        if n is None:
            break
        
        print(f"\nFactoring n = {n}")
        print(f"Bit length: {n.bit_length()} bits")
        
        # Check if number is prime first
        if gmpy2.is_prime(n):
            print("The number is prime! No factorization needed.")
            continue
        
        # Check if number is even
        if n % 2 == 0:
            print("Number is even. Using simple division...")
            p = mpz(2)
            q = n // 2
            print(f"Factors found: {n} = {p} * {q}")
            continue
        
        # Get max iterations from user
        try:
            max_iter = input("Enter maximum iterations (default 100000): ").strip()
            max_iterations = int(max_iter) if max_iter else 100000
        except:
            max_iterations = 100000
            print("Using default 100000 iterations")
        
        print(f"\nStarting Fermat factorization with max {max_iterations} iterations...")
        
        # Try basic method first
        print("\n1. Basic Fermat method:")
        result1 = fermat_factorization(n, max_iterations)
        if result1:
            p, q = result1
            print_rsa_components(n,p,q)
        else:
            print("✗ No factors found with basic method")
        
        # Try optimized method
        print("\n2. Optimized Fermat method:")
        result2 = fermat_factorization_optimized(n, max_iterations)
        if result2:
            p, q = result2
            print_rsa_components(n,p,q)
        else:
            print("✗ No factors found with optimized method")
        
        # Try with statistics
        print("\n3. Fermat method with statistics:")
        result3 = fermat_factorization_with_stats(n, max_iterations)
        if result3['success']:
            p, q = result3['factors']
            print_rsa_components(n,p,q)
            print(f"  Iterations: {result3['iterations']}")
            print(f"  Distance from √n: {result3['distance']}")
            
            
            # Additional info for RSA context
            if p.bit_length() == q.bit_length():
                print(f"  Note: Factors have same bit length ({p.bit_length()} bits) - vulnerable to Fermat!")
            else:
                print(f"  Factor bit lengths: {p.bit_length()} and {q.bit_length()} bits")
        else:
            print(f"✗ No factors found in {result3['iterations']} iterations")
            print(f"  Last x tried: {result3['final_x']}")
            print(f"  Distance reached: {result3['distance']}")
            
            # Give user advice
            if result3['distance'] < 1000:
                print("  Hint: Factors might be very close! Try increasing iterations.")
            else:
                print("  Hint: Factors might be too far apart for Fermat method.")
                print("  Consider using other factorization methods like Pollard's Rho.")
        
        print("\n" + "=" * 60)

# Example usage with test cases
def run_test_cases():
    """
    Run predefined test cases to verify the algorithm works
    """
    test_cases = [
        mpz(5959),      # 59 * 101
        mpz(2881),      # 43 * 67
        mpz(187),       # 11 * 17
        mpz(15),        # 3 * 5
        mpz(21),        # 3 * 7
    ]
    
    print("Predefined Test Cases:")
    print("=" * 50)
    
    for n in test_cases:
        print(f"\nFactoring n = {n}")
        result = fermat_factorization_optimized(n)
        if result:
            p, q = result
            print(f"✓ {n} = {p} * {q}")
        else:
            print(f"✗ No factors found")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Run test cases")
    print("2. Enter custom number to factorize")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        run_test_cases()
    else:
        main()
