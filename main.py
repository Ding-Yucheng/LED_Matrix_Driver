import machine
import time
from machine import Pin,SoftSPI

def create_inverted_triangle_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        num_zeros = i
        num_ones = size - i
        row.extend([0] * num_ones)
        row.extend([1] * num_zeros)
        matrix.append(row)
    return matrix

def binary_list_to_byte(bin_list):                            
    return int(''.join(str(bit) for bit in bin_list), 2)

def col_data_assign(row):
    for MUX in MUX_list:
        MUX.value(0)
    for i in range(4):
        SYNC_list[i].value(0)
        spi714.write(bytes_matrix[row][i])
        SYNC_list[i].value(1)

def row_select(row):
    temp = int(row / 16)
    row %= 16
    for i in range(4):
        MA_list[i].value(row % 2)
        row = int(row / 2) 
    MUX_list[temp].value(1)

# Define Pins
MUX1 = machine.Pin(27, machine.Pin.OUT)
MUX2 = machine.Pin(14, machine.Pin.OUT)
MUX_list = [MUX1, MUX2]

MA0 = machine.Pin(32, machine.Pin.OUT)
MA1 = machine.Pin(33, machine.Pin.OUT)
MA2 = machine.Pin(25, machine.Pin.OUT)
MA3 = machine.Pin(26, machine.Pin.OUT)
MA_list = [MA0, MA1, MA2, MA3]


CLK = machine.Pin(18, machine.Pin.OUT)

RST = machine.Pin(13, machine.Pin.OUT) 

DIN = machine.Pin(23, machine.Pin.OUT) 
DOUT = machine.Pin(19, machine.Pin.OUT) 

SYNC1 = machine.Pin(22, machine.Pin.OUT)
SYNC2 = machine.Pin(21, machine.Pin.OUT)
SYNC3 = machine.Pin(17, machine.Pin.OUT)
SYNC4 = machine.Pin(16, machine.Pin.OUT)
SYNC_list = [SYNC1, SYNC2, SYNC3, SYNC4]

# Multiswitch SPI setup
spi714 = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))

# Initialize
RST.value(0)           
time.sleep_us(1)
RST.value(1)

for MUX in MUX_list:   
    MUX.value(0)

for SYNC in SYNC_list: 
    SYNC.value(1)
# Raw data input

#picture_matrix = create_inverted_triangle_matrix(32) # Calibration
#picture_matrix = [[1 if i == j else 0 for j in range(32)] for i in range(32)] # diagonal
#picture_matrix = [[1 if i % 2 == 0 else 0 for _ in range(32)] for i in range(32)] # horizontal stripes
#picture_matrix = [[1 if (i + j) % 2 == 0 else 0 for j in range(32)] for i in range(32)] # checkerboard
picture_matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] # HKUST Logo

# Transformation of row data
row_order = [17, 15, 16, 14, 18, 13, 19, 12, 20, 11, 21, 10, 22, 9, 23, 8, 24, 0, 25, 7, 26, 6, 27, 5, 28, 4, 29, 3, 30, 2, 31, 1]
reordered_picture_matrix = [picture_matrix[row] for row in row_order]

col_order = [4, 28, 2, 29, 1, 30, 0, 31, 7, 24, 6, 25, 5, 26, 3, 27, 11, 21, 10, 20, 9, 22, 8, 23, 15, 16, 14, 17, 13, 19, 12, 18]
final_picture_matrix = [[reordered_picture_matrix[row][col] for col in col_order] for row in range(32)]

bytes_matrix = []
for row in final_picture_matrix:
    byte_row = []
    for i in range(0, 32, 8):
        byte_row.append(binary_list_to_byte(row[i:i+8]))
    bytes_row = [bytes([byte]) for byte in byte_row]
    bytes_matrix.append(bytes_row)
    
# Display of picture
while 1:
    try:
        for i in range(32):
            col_data_assign(i)
            row_select(i)
            time.sleep_us(1)       
    except:
        print('error')
        break
    
