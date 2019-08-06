from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import InputForm
from django.views import generic
# Create your views here.

def result(request):
    return render(request, 'result.html')



def home(request):
    if request.method == 'POST':
        form = InputForm(request.POST)

        if form.is_valid():
            input = form.cleaned_data['input']
            matrix = parseIntoMatrix(input)
            add = addMatricies(matrix,matrix)
            sub = subMatricies(matrix,matrix)
            mult = multiplyMatrices(len(matrix),matrix,matrix)

            return redirect('result')
            # return HttpResponse('Matrix:<br/> %s <br/><br/> Added to itself:<br/> %s <br/><br/> Substracted to itself:<br/> %s <br/><br/> Multiplied to itself:<br/> %s' % (matrix,add,sub,mult))
            print('Matrix:')
            printMatrix(matrix)

            print('\nAdded to itself:')
            printMatrix(addMatricies(matrix,matrix))

            print('\nSubtracted from itself:')
            printMatrix(subMatricies(matrix,matrix))

            print('\nMultiplied by itself:')
            printMatrix(multiplyMatrices(len(matrix),matrix,matrix))

        else:
            return HttpResponseRedirect('/') #FAILED LOGIN, BACK TO LOGIN FORM
    else:
        form = InputForm()

    return render(request, 'home.html', {'form': form})


# function to create a zero matrix of size n
# returns a matrix
def zeroMatrix(n):
    matrix = []
    if n >= 1:
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            matrix.append(row)
    return matrix

# funtion to add 2 matricies
# returns a matrix
def addMatricies(a,b):
    n = len(a)
    sum = zeroMatrix(n)
    for i in range(n):
        for j in range(n):
            sum[i][j] = a[i][j] + b[i][j]
    return sum

#funtion to subtract 2 matricies
# returns a matrix
def subMatricies(a,b):
    n = len(a)
    sum = zeroMatrix(n)
    for i in range(n):
        for j in range(n):
            sum[i][j] = a[i][j] - b[i][j]
    return sum

# function to multiply two matrices of size n
# returns a matrix
def multiplyMatrices(n,m1,m2):
   result = []
   if m1 and m2:
       result = zeroMatrix(n)
       for i in range(n):
            for j in range(n):
                 for k in range(n):
                        result[i][j] += m1[i][k] * m2[k][j]
   return result
def printMatrix(matrix):
    if matrix:
        for i in matrix:
            for j in i:
                print(j, " ", end="")
            print()
    return

def parseIntoMatrix(input):
    print('parser working...')
    matrix = list()
    for line in input.split():
        matrix.append(list(map(int,line.split(','))))
    return matrix
def parseIntoStr(matrix):
    matrixStr = ''
    for row in matrix:
        matrixStr += str(row)+'\n'
    return matrixStr
