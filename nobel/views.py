from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from .Query import All_Queries, Mapper

import pandas as pd
from pandas.io.json import json_normalize
from SPARQLWrapper import SPARQLWrapper, JSON
#=============QUERY ENGINE
def Query_Engine(sparql_query):
    Sparql_Endpoint = 'http://DESKTOP-VMDFKGL:7200/repositories/Climate_Ontology'
    sparql = SPARQLWrapper(Sparql_Endpoint, agent="SparqlWrapper")  
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(JSON)
    result = sparql.query().convert()
    result_table = pd.json_normalize(result["results"]["bindings"])
    valuse_list = []
    for i in result_table:
        a = i.split('.')
        if a[1]=='value':
            valuse_list.append(i)
    Query_data = result_table[valuse_list]
    names = []
    result = []     
    for col in Query_data:
        names.append(col.split(".")[0])  
               
    for row in range(len(Query_data.values)):
        data = []
        for col in Query_data:
            data.append(Query_data.iloc[row][col])
        result.append(data)    
    return names, result

#=============================LOGO IN=========================
def logInUser(request):
    if request.method=='GET':
        return render(request, 'nobel/logInUser.html', {
            'form': AuthenticationForm()
        })
    elif request.method=='POST':
        user = authenticate(request, 
            username=request.POST['username'], 
            password=request.POST['password']
        )
        if user is None:
            messages.error(request, 'Please Enter Correct Name or Password')
            return render(request, 'nobel/logInUser.html', {
                'form': AuthenticationForm()
            })
        else:
            login(request, user)
            return redirect('board')

@login_required(redirect_field_name='LogInUser')
def logOutUser(request):
    if request.method=='GET':
        logout(request)
        return redirect('LogInUser')
    
#=================================================================

@login_required(redirect_field_name='LogInUser')      
def dashboard(request):
    return render(request, 'nobel/dashboard.html', {
        'Mapper': Mapper,
    })

@login_required(redirect_field_name='LogInUser')      
def selectQueryResult(request, id):
    if request.method=='GET':
        Query = All_Queries[id]
        Column_names = []
        Column_result = []
        Column_names, Column_result = Query_Engine(Query)  
        return render(request, 'nobel/selectedResult.html', {
            'Col_names': Column_names,
            'Col_res': Column_result,
        })


@login_required(redirect_field_name='LogInUser')      
def sparqlEndpoint(request):
    return render(request, 'nobel/sparql.html', {})

@login_required(redirect_field_name='LogInUser')      
def queryResult(request):
    if request.method=='POST':
        Query = request.POST['Query']
        Column_names = []
        Column_result = []
        try:
            Column_names, Column_result = Query_Engine(Query)
        except:
            messages.error(request, 'Please Enter Correct Query !')
            return render(request, 'nobel/sparql.html', {})
        return render(request, 'nobel/result.html', {
            'Col_names': Column_names,
            'Col_res': Column_result,
        })
    return redirect('sparqlEnd')