from mpmath import *
mp.dps = 500; mp.pretty = True

print(+pi)
#180*degree
#4*atan(1)
#16*acot(5)-4*acot(239)
#48*acot(49)+128*acot(57)-20*acot(239)+48*acot(110443)
#chop(2*j*log((1-j)/(1+j)))
#chop(-2j*asinh(1j))
#chop(ci(-inf)/1j)
#gamma(0.5)**2
#beta(0.5,0.5)
#(2/diff(erf, 0))**2
#findroot(sin, 3)
#findroot(cos, 1)*2
#chop(-2j*lambertw(-pi/2))
#besseljzero(0.5,1)
#3*sqrt(3)/2/hyp2f1((-1,3),(1,3),1,1)
#8/(hyp2f1(0.5,0.5,1,0.5)*gamma(0.75)/gamma(1.25))**2
#4*(hyp1f2(1,1.5,1,1) / struvel(-0.5, 2))**2
#1/meijerg([[],[]], [[0],[0.5]], 0)**2
#(meijerg([[],[2]], [[1,1.5],[]], 1, 0.5) / erfc(1))**2
#(1-e) / meijerg([[1],[0.5]], [[1],[0.5,0]], 1)
#sqrt(psi(1,0.25)-8*catalan)
#elliprc(1,2)*4
#elliprg(0,1,1)*4
#2*agm(1,0.5)*ellipk(0.75)
#(gamma(0.75)*jtheta(3,0,exp(-pi)))**4
#cbrt(gamma(0.25)**4*agm(1,sqrt(2))**2/8)
#sqrt(6*zeta(2))
#sqrt(6*(zeta(2,3)+5./4))
#sqrt(zeta(2,(3,4))+8*catalan)
#exp(-2*zeta(0,1,1))/2
#sqrt(12*altzeta(2))
#4*dirichlet(1,[0,1,0,-1])
#2*catalan/dirichlet(-1,[0,1,0,-1],1)
#exp(-dirichlet(0,[0,1,0,-1],1))*gamma(0.25)**2/(2*sqrt(2))
#sqrt(7*zeta(3)/(4*diff(lerchphi, (-1,-2,1), (0,1,0))))
#sqrt(-12*polylog(2,-1))
#sqrt(6*log(2)**2+12*polylog(2,0.5))
#chop(root(-81j*(polylog(3,root(1,3,1))+4*zeta(3)/9)/2,3))
#2*clsin(1,1)+1
#(3+sqrt(3)*sqrt(1+8*clcos(2,1)))/2
#root(2,6)*sqrt(e)/(glaisher**6*barnesg(0.5)**4)
#nsum(lambda k: 4*(-1)**(k+1)/(2*k-1), [1,inf])
#nsum(lambda k: (3**k-1)/4**k*zeta(k+1), [1,inf])
#nsum(lambda k: 8/(2*k-1)**2, [1,inf])**0.5
#nsum(lambda k: 2*fac(k)/fac2(2*k+1), [0,inf])
#nsum(lambda k: fac(k)**2/fac(2*k+1), [0,inf])*3*sqrt(3)/2
#nsum(lambda k: fac(k)**2/(phi**(2*k+1)*fac(2*k+1)), [0,inf])*(5*sqrt(phi+2))/2
#nsum(lambda k: (4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))/16**k, [0,inf])
#2/nsum(lambda k: (-1)**k*(4*k+1)*(fac2(2*k-1)/fac2(2*k))**3, [0,inf])
#nsum(lambda k: 72/(k*expm1(k*pi))-96/(k*expm1(2*pi*k))+24/(k*expm1(4*pi*k)), [1,inf])
#1/nsum(lambda k: binomial(2*k,k)**3*(42*k+5)/2**(12*k+4), [0,inf])
#4/nsum(lambda k: (-1)**k*(1123+21460*k)*fac2(2*k-1)*fac2(4*k-1)/(882**(2*k+1)*32**k*fac(k)**3), [0,inf])
#9801/sqrt(8)/nsum(lambda k: fac(4*k)*(1103+26390*k)/(fac(k)**4*396**(4*k)), [0,inf])
#426880*sqrt(10005)/nsum(lambda k: (-1)**k*fac(6*k)*(13591409+545140134*k)/(fac(k)**3*fac(3*k)*(640320**3)**k), [0,inf])
#4/nsum(lambda k: (6*k+1)*rf(0.5,k)**3/(4**k*fac(k)**3), [0,inf])
#(ln(8)+sqrt(48*nsum(lambda m,n: (-1)**(m+n)/(m**2+n**2), [1,inf],[1,inf]) + 9*log(2)**2))/2
#-nsum(lambda x,y: (-1)**(x+y)/(x**2+y**2), [-inf,inf], [-inf,inf], ignore=True)/ln2
#2*nsum(lambda k: sin(k)/k, [1,inf])+1
#quad(lambda x: 2/(x**2+1), [0,inf])
#quad(lambda x: exp(-x**2), [-inf,inf])**2
#2*quad(lambda x: sqrt(1-x**2), [-1,1])
#chop(quad(lambda z: 1/(2j*z), [1,j,-1,-j,1]))
#3*(4*log(2+sqrt(3))-quad(lambda x,y: 1/sqrt(1+x**2+y**2), [-1,1],[-1,1]))/2
#sqrt(8*quad(lambda x,y: 1/(1-(x*y)**2), [0,1],[0,1]))
#sqrt(6*quad(lambda x,y: 1/(1-x*y), [0,1],[0,1]))
#sqrt(6*quad(lambda x: x/expm1(x), [0,inf]))
#quad(lambda x: (16*x-16)/(x**4-2*x**3+4*x-4), [0,1])
#quad(lambda x: sqrt(x-x**2), [0,0.25])*24+3*sqrt(3)/4
#mpf(22)/7 - quad(lambda x: x**4*(1-x)**4/(1+x**2), [0,1])
#mpf(355)/113 - quad(lambda x: x**8*(1-x)**8*(25+816*x**2)/(1+x**2), [0,1])/3164
#2*quadosc(lambda x: sin(x)/x, [0,inf], omega=1)
#40*quadosc(lambda x: sin(x)**6/x**6, [0,inf], omega=1)/11
#e*quadosc(lambda x: cos(x)/(1+x**2), [-inf,inf], omega=1)
#8*quadosc(lambda x: cos(x**2), [0,inf], zeros=lambda n: sqrt(n))**2
#2*quadosc(lambda x: sin(exp(x)), [1,inf], zeros=ln)+2*si(e)
#exp(2*quad(loggamma, [0,1]))/2
#2*nprod(lambda k: sec(pi/2**k), [2,inf])
#s=lambda k: sqrt(0.5+s(k-1)/2) if k else 0; 2/nprod(s, [1,inf])
#s=lambda k: sqrt(2+s(k-1)) if k else 0; limit(lambda k: sqrt(2-s(k))*2**(k+1), inf)
#2*nprod(lambda k: (2*k)**2/((2*k-1)*(2*k+1)), [1,inf])
#2*nprod(lambda k: (4*k**2)/(4*k**2-1), [1, inf])
#sqrt(6*ln(nprod(lambda k: exp(1/k**2), [1,inf])))
#nprod(lambda k: (k**2-1)/(k**2+1), [2,inf])/csch(pi)
#nprod(lambda k: (k**2-1)/(k**2+1), [2,inf])*sinh(pi)
#nprod(lambda k: (k**4-1)/(k**4+1), [2, inf])*(cosh(sqrt(2)*pi)-cos(sqrt(2)*pi))/sinh(pi)
#sinh(pi)/nprod(lambda k: (1-1/k**4), [2, inf])/4
#sinh(pi)/nprod(lambda k: (1+1/k**2), [2, inf])/2
#(exp(1+euler/2)/nprod(lambda n: (1+1/n)**n * exp(1/(2*n)-1), [1, inf]))**2/2
#3*sqrt(2)*cosh(pi*sqrt(3)/2)**2*csch(pi*sqrt(2))/nprod(lambda k: (1+1/k+1/k**2)**2/(1+2/k+3/k**2), [1, inf])
#2/e*nprod(lambda k: (1+2/k)**((-1)**(k+1)*k), [1,inf])
#limit(lambda k: 16**k/(k*binomial(2*k,k)**2), inf)
#limit(lambda x: 4*x*hyp1f2(0.5,1.5,1.5,-x**2), inf)
#1/log(limit(lambda n: nprod(lambda k: pi/(2*atan(k)), [n,2*n]), inf),4)
#limit(lambda k: 2**(4*k+1)*fac(k)**4/(2*k+1)/fac(2*k)**2, inf)
#limit(lambda k: fac(k) / (sqrt(k)*(k/e)**k), inf)**2/2
#limit(lambda k: (-(-1)**k*bernoulli(2*k)*2**(2*k-1)/fac(2*k))**(-1/(2*k)), inf)
#limit(lambda k: besseljzero(1,k)/k, inf)
#1/limit(lambda x: airyai(x)*2*x**0.25*exp(2*x**1.5/3), inf, exp=True)**2
#1/limit(lambda x: airybi(x)*x**0.25*exp(-2*x**1.5/3), inf, exp=True)**2
