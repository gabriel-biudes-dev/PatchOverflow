def find_data(file_path):
    """
    Searches for the byte sequence '25 xx xx 73 00' in a binary file, where 'xx' can be any byte.
    
    :param file_path: Path to the binary file.
    :return: List of starting indexes where the pattern occurs.
    """
    pattern = [0x25, 0x00, 0x00, 0x73, 0x00]  # The fixed byte sequence with 'xx' being any byte
    indexes = []

    try:
        with open(file_path, "rb") as file:
            content = file.read()  # Read the entire file into memory
            
            # Search for the pattern in the file
            for i in range(len(content) - len(pattern) + 1):
                if (content[i] == pattern[0] and 
                    content[i + 3] == pattern[3] and 
                    content[i + 4] == pattern[4]):
                    # Check for the 0x25 at the beginning, 0x73 at the 4th byte, and 0x00 at the 5th byte
                    # Skip the 2nd and 3rd byte positions (these can be anything)
                    indexes.append(i)  # Store the starting index of the match
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return indexes


def view_bytes(file_path, start_index, byte_count):
    """
    Displays a range of bytes from the binary file, starting from the given index.
    
    :param file_path: Path to the binary file.
    :param start_index: The index in the file where to start reading.
    :param byte_count: The number of bytes to read from the start index.
    """
    try:
        with open(file_path, "rb") as file:
            # Move to the start index
            file.seek(start_index)
            
            # Read the specified number of bytes
            byte_data = file.read(byte_count)
            
            if byte_data:
                print(f"Bytes from index {start_index - byte_count} (showing {byte_count} bytes):")
                
                # Display bytes in hexadecimal and ASCII format
                hex_rep = ' '.join([f"{byte:02x}" for byte in byte_data])
                ascii_rep = ''.join([chr(byte) if 32 <= byte <= 126 else '.' for byte in byte_data])
                
                print(f"Hex: {hex_rep}")
                print(f"ASCII: {ascii_rep}")
            else:
                print(f"No data found.")
                
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def view_byte_at_position(file_path, position):
    """
    Displays the byte at a specific position in the binary file.
    
    :param file_path: Path to the binary file.
    :param position: The position (index) in the file where the byte is located.
    """
    try:
        with open(file_path, "rb") as file:
            # Move to the specific position in the file
            file.seek(position)
            
            # Read the byte at that position
            byte_data = file.read(1)  # Read one byte
            
            if byte_data:
                # Display the byte in hexadecimal and ASCII format
                print(f"Byte at position {position}:")
                print(f"Hex: {byte_data.hex()}")
                print(f"ASCII: {chr(byte_data[0]) if 32 <= byte_data[0] <= 126 else '.'}")
            else:
                print(f"No data found at position {position}.")
                
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def write_byte_at_position(file_path, position, hex_value):
    """
    Writes a byte at a specific position in the binary file, with the byte value provided in hexadecimal.
    
    :param file_path: Path to the binary file.
    :param position: The position (index) in the file where the byte should be written.
    :param hex_value: The byte (as a hexadecimal string, e.g., '0x45') to write at the given position.
    """
    try:
        # Convert the hex_value from string to an integer (if necessary)
        if isinstance(hex_value, str):
            hex_value = int(hex_value, 16)  # Convert from hex string to int
        
        # Ensure hex_value is a single byte (an integer between 0 and 255)
        if not (0 <= hex_value <= 255):
            raise ValueError("hex_value must be an integer between 0 and 255.")
        
        with open(file_path, "r+b") as file:
            # Move to the specific position in the file
            file.seek(position)
            
            # Write the byte at that position
            file.write(bytes([hex_value]))  # Write the byte
            
            print(f"Byte {hex(hex_value)} written at position {position}.")
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to execute the workflow: search for the pattern, view bytes before and after the match,
    and modify the file.
    """
    file_path = input("Enter the file path: ")
    ind = find_data(file_path)

    for index in ind:
        print('Size variable found: ')
        # View 5 bytes from the match
        view_bytes(file_path, index, 5)
        
        # Modify the file by writing new values at specific positions
        write_byte_at_position(file_path, index + 1, 0x39)
        write_byte_at_position(file_path, index + 2, 0x39)
        
        print('Vuln injection successful')

if __name__ == "__main__":
    main()
