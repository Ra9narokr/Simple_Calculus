from scipy.integrate import quad

def integrate_average(f, a, b):
    integral, _ = quad(f, a, b)
    return integral / (b - a)
