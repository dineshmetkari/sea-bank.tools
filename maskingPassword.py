import random
import itertools
import time

PASS_LENGTH = 12
MASK_MIN_LENGTH = 4
MASK_MAX_LENGTH = 6
MASKS_COUNT = 20
OVERHEARS_MAX = 10
REPETITION_COUNT = 1000000
LOGIN_ATTEMPTS_NUMBER = 10

def masks():
    for i in xrange(MASK_MIN_LENGTH,MASK_MAX_LENGTH+1):
        for mask in itertools.combinations(xrange(PASS_LENGTH), i):
            yield mask

def overhear(overhears_count, masks):
    password = [False for _ in range(PASS_LENGTH)]
    for _ in xrange(overhears_count):
        for i in random.choice(masks):
            password[i] = True
    return password

def login(password, masks):
    for i in random.choice(masks):
        if password[i] == False:
            return False

    return True

def get_density_and_probability (overhears_count, masks):
    density = [0L for _ in xrange(PASS_LENGTH + 1)]
    probability = 0L

    for _ in xrange(REPETITION_COUNT):
        password = overhear(overhears_count, masks)
        density[sum(password)]+=1

        for _ in xrange(LOGIN_ATTEMPTS_NUMBER):
            if login(password, masks):
                probability += 1
    return (density, probability)

def reverse_distribution(fun):
    for i in xrange(len(fun)):
        yield sum(fun[i:len(fun)]);

def format_density (density):
    output = ""
    for s in (reverse_distribution(density)):
        output += "%7.2f%%, "%(float(s)/REPETITION_COUNT*100)
    return output

def format_probability (probability):
    return "%7.3f%%"%(float(probability)/REPETITION_COUNT/LOGIN_ATTEMPTS_NUMBER*100)


ts = time.time()
masks = list(masks());
if MASKS_COUNT > 0:
    masks = random.sample(masks, MASKS_COUNT)

print "Dlugosc hasla: %i"%(PASS_LENGTH)
print "Rozmiar maski: od %i do %i"%(MASK_MIN_LENGTH, MASK_MAX_LENGTH)
print "Liczba masek: %i"%(len(masks))
print "Liczba powtorzen: %i"%(REPETITION_COUNT)
print "Liczba prob logowania: %i"%(REPETITION_COUNT * LOGIN_ATTEMPTS_NUMBER)
print ""

header = ""
for i in xrange(PASS_LENGTH+1):
    header += "%5i     "%i

print "Liczba zdobytych cyfr: %s P-stwo logowania:"%(header)

for overhears_count in xrange(1,OVERHEARS_MAX + 1):    
    density, probability = get_density_and_probability (overhears_count, masks);
    print "Liczba podsluchan %3i: %s %17s"%(overhears_count, format_density(density), format_probability(probability))

te = time.time()

print ""
print 'Czas obliczen: %2.2f sekund' % (te-ts)