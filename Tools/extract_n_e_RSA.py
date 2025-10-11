from Cryptodome.PublicKey import RSA
import os

def get_rsa_key_components():
    """
    Extract RSA modulus (n) and public exponent (e) from a public key file
    """
    try:
        # Get file path from user
        file_path = input("Enter the path to your RSA public key file: ").strip()
        
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found.")
            return
        
        # Read and import the public key
        with open(file_path, 'r') as f:
            public_key_data = f.read()
        
        # Import the key
        pub_key = RSA.importKey(public_key_data)
        
        # Access the modulus (n) and exponent (e)
        print("\n" + "="*50)
        print("RSA PUBLIC KEY COMPONENTS")
        print("="*50)
        print(f"Modulus (n):\n{pub_key.n}")
        print(f"\nPublic Exponent (e): {pub_key.e}")
        print("="*50)
        
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except PermissionError:
        print("Error: Permission denied to read the file.")
    except ValueError as ve:
        print(f"Error: Invalid key format - {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    """
    Main function to run the RSA key component extractor
    """
    print("RSA Public Key Component Extractor")
    print("This tool extracts modulus (n) and exponent (e) from RSA public keys")
    
    while True:
        get_rsa_key_components()
        
        # Ask if user wants to continue
        continue_choice = input("\nDo you want to analyze another key? (y/n): ").strip().lower()
        if continue_choice not in ['y', 'yes']:
            print("Goodbye!")
            break
        print("\n" + "-"*50)

if __name__ == "__main__":
    main()
