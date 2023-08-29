import numpy as np
import matplotlib.pyplot as plt
import random
from colorama import init, Fore
from mpl_toolkits.mplot3d import axes3d
init()
def extract_coefficients(expr):
    # Check if the input is a string
    if isinstance(expr, str):
        coefficients = []
        for coef_str in expr.split(","):
            coefficients.append(int(coef_str))
        return coefficients
    else:
        raise TypeError("Input should be a string of coefficients separated by commas.")

def polynomial(coefficients, x):
    # Calculate the polynomial equation
    return sum(c * x**i for i, c in enumerate(reversed(coefficients)))

def draw_graph(expr):
    fig, ax = plt.subplots()  # Initialize the plot
    x = np.linspace(-10, 10, 400)
    try:
        coefficients = extract_coefficients(expr)
        # Calculate y based on the polynomial equation
        y = polynomial(coefficients, x)
        ax.plot(x, y)
        plt.show()
    except Exception as e:
        print("Error", f"An error occurred: {e}")

def random_dis(max1,r):
    random_numbers = [0] * r
    for ii in range(r):
        random_numbers[ii] = random.randint(1, max1)
        print(Fore.GREEN + f'\rWalnut@terminal:~$ {ii}: {random_numbers[ii]}' + Fore.RESET)
        

    counts = [0] * max1
    for i in range(1, max1+1):
        counts[i-1] = random_numbers.count(i)
    plt.bar(range(1, max1+1), counts)
    plt.ylabel('Counts')
    plt.xlabel('Numbers')
    plt.title('Random Number Distribution')
    plt.xticks(range(1, max1+1))
    plt.show()

def tdplt():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # 產生測試資料
    X, Y, Z = axes3d.get_test_data(0.05)

    # 繪製 3D 曲面圖形
    ax.plot_surface(X, Y, Z, cmap='seismic')

    # 顯示圖形
    plt.show()

def vector():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # 產生格點資料
    x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                        np.arange(-0.8, 1, 0.2),
                        np.arange(-0.8, 1, 0.8))

    # 產生向量場資料
    u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
    v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
    w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
        np.sin(np.pi * z))

    # 繪製向量場
    ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)

    # 顯示圖形
    plt.show()


