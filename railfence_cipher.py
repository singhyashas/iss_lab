def encrypt_rail_fence(plaintext, rails):

   # Create the matrix for cipher
   rail_matrix = [['\n' for i in range(len(plaintext))]
   for j in range(rails)]
	
   # Find the direction
   down_direction = False
   row, col = 0, 0
	
   for i in range(len(plaintext)):
		
      # Check the direction of flow
      # Reverse the direction if just filled the top or bottom rail
      if (row == 0) or (row == rails - 1):
         down_direction = not down_direction
		
         # Fill the corresponding alphabet
         rail_matrix[row][col] = plaintext[i]
         col += 1
		
         # Find the next row using direction flag
         if down_direction:
            row += 1
         else:
            row -= 1
	
   # Construct the cipher using the rail matrix
   cipher_text = []
   for i in range(rails):
      for j in range(len(plaintext)):
         if rail_matrix[i][j] != '\n':
            cipher_text.append(rail_matrix[i][j])
      return("" . join(cipher_text))
	
# Function to decrypt the cipher-text
# Function to decrypt the cipher-text
def decrypt_rail_fence(cipher, rails):

   # Create the matrix to cipher
   # plaintext - rows, length(cipher) - columns
   # Fill the rail matrix to distinguish filled spaces from blank ones
   rail_matrix = [['\n' for i in range(len(cipher))]
   for j in range(rails)]
	
   # Find the direction
   down_direction = None
   row, col = 0, 0
	
   for i in range(len(cipher)):
		
      # Check the direction of flow
      if row == 0:
         down_direction = True
      if row == rails - 1:
         down_direction = False
		
      # Place the cipher text in the rail matrix
      rail_matrix[row][col] = '*'
      col += 1
		
      # Find the next row using direction flag
      if down_direction:
         row += 1
      else:
         row -= 1
			
   # Reconstruct the rail matrix with cipher text
   index = 0
   for i in range(rails):
      for j in range(len(cipher)):
         if rail_matrix[i][j] == '*' and index < len(cipher):
            rail_matrix[i][j] = cipher[index]
            index += 1
				
   # Read the rail matrix in zig-zag manner to construct the resultant text
   result = []
   row, col = 0, 0
   for i in range(len(cipher)):
		
      # Check the direction of flow
      if row == 0:
         down_direction = True
      if row == rails - 1:
         down_direction = False
			
      # Add characters from the rail matrix to the result
      if rail_matrix[row][col] != '*':
         result.append(rail_matrix[row][col])
         col += 1
			
      # Find the next row using direction flag
      if down_direction:
         row += 1
      else:
         row -= 1
	
      return ''.join(result)

# Driver code
if __name__ == "__main__":
   print("First Encrypted Text: ", encrypt_rail_fence("Hello Tutorialspoint", 2))
   print("Second Encrypted Text: ", encrypt_rail_fence("Simple Text", 3))
   print("Third Encrypted Text: ", encrypt_rail_fence("I am great Cipher", 5))
   # Decryption of the cipher-text
   print("First Decrypted Text: ", decrypt_rail_fence("HloTtrasonel uoilpit", 2))
   print("Second Decrypted Text: ", decrypt_rail_fence("SleipeTxm t", 3))
   print("Third Decrypted Text: ", decrypt_rail_fence("Iar etear hmgCp i", 5))