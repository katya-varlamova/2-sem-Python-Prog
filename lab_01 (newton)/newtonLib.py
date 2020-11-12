def f(x):
    return x*x*x + 2*x -1#x*x*x - 2*x  + x*x - 2
# Newton-Raphson method
def newton(func, x0, fprime=None, args=(), tol=1.48e-8, maxiter=50,
           fprime2=None):
    if tol <= 0:
        raise ValueError("tol too small (%g <= 0)" % tol)
    if fprime is not None:
        p0 = 1.0 * x0
        fder2 = 0
        for iter in range(maxiter):
            myargs = (p0,) + args
            fder = fprime(*myargs)
            if fder == 0:
                msg = "derivative was zero."
                warnings.warn(msg, RuntimeWarning)
                return p0
            fval = func(*myargs)
            if fprime2 is not None:
                fder2 = fprime2(*myargs)
            if fder2 == 0:
                # Newton step
                p = p0 - fval / fder
            else:
                # Parabolic Halley's method
                discr = fder ** 2 - 2 * fval * fder2
                if discr < 0:
                    p = p0 - fder / fder2
                else:
                    p = p0 - 2*fval / (fder + sign(fder) * sqrt(discr))
            if abs(p - p0) < tol:
                return p
            p0 = p
    else:
        # Secant method
        p0 = x0
        if x0 >= 0:
            p1 = x0*(1 + 1e-4) + 1e-4
        else:
            p1 = x0*(1 + 1e-4) - 1e-4
        q0 = func(*((p0,) + args))
        q1 = func(*((p1,) + args))
        for iter in range(maxiter):
            if q1 == q0:
                if p1 != p0:
                    msg = "Tolerance of %s reached" % (p1 - p0)
                    warnings.warn(msg, RuntimeWarning)
                return (p1 + p0)/2.0
            else:
                p = p1 - q1*(p1 - p0)/(q1 - q0)
            if abs(p - p1) < tol:
                return p
            p0 = p1
            q0 = q1
            p1 = p
            q1 = func(*((p1,) + args))
    msg = "Failed to converge after %d iterations, value is %s" % (maxiter, p)
    raise RuntimeError(msg)
print(newton(f, 0))
