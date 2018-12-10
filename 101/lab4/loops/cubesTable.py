# CPE 101 Lab 4
# Name: Sydney Jaques

def main():
   table_size = get_table_size()
   while table_size != 0:
      first = get_first()
      increment = get_increment()
      show_table(table_size, first, increment)
      table_size = get_table_size()

# Obtain a valid table size from the user
def get_table_size():
   size = int(input("Enter number of rows in table (0 to end): "))

   while size < 0:
      print("Size must be non-negative.")
      size = int(input("Enter number of rows in table (0 to end): "))
      
   return size;

# Obtain the first table entry from the user 
def get_first():
   first = int(input("Enter the value of the first number in the table: "))

   while first < 0:
      print("First number must be non-negative.")
      first = int(input("Enter the value of the first number in the table: "))
   return first

# Display the table of cubes
def show_table(size, first, increment):
   print("A cube table of size %d will appear here starting with %d." % (size, first))
   print("Number  Cube")
   # Insert Loop Here
   num = first
   sum = 0
   for i in range(size):
      print("%-6d %d" %(num, num**3))
      sum += num ** 3
      num = num + increment
   print("The sum of cubes is:", sum)
      

#enhancement#3
def get_increment():
   increment = int(input("Enter the increment between rows: "))
   if increment < 0:
      print("Increment must be non-negative.")
      increment = int(input("Enter the increment between rows: "))
      
   return increment
   
   


if __name__ == "__main__":
   main()
