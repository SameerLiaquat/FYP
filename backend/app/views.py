#views.py
import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.parse

from .queryengine import FederatedQuery, Sparql_Endpoint, competencyquestion1, constructCommentarySparQLQueryString, constructCommentarySparQLQueryString_fullgraph, constructCommentarySparQLQueryString_fullgraph2, constructCommentarySparQLQueryString_fullgraph3, constructHadithSparQLQueryString_fullgraph, constructHadithSparQLQueryString_fullgraph_2, constructHadithSparQLQueryString_fullgraph_3,constructVerseSparQLQueryString_fullgraph,constructVerseSparQLQueryString_fullgraph2,constructVerseSparQLQueryString_fullgraph3,constructVerseSparQLQueryString_fullgraph4,constructVerseSparQLQueryString_fullgraph5, getNarratorChain, FederatedQuery_2,FederatedQuery_3,FederatedQuery1_2 ,FederatedQuery1_3, competencyquestion2, competencyquestion3, competencyquestion4, competencyquestion5, competencyquestion6, competencyquestion7, competencyquestion8, competencyquestion9, competencyquestion10, competencyquestion11, competencyquestion12

class ReactView(APIView):
    print('sadsada')

@csrf_exempt
def query_hadith(request):
    print('backend/POST')
    print(request.body)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request body'}, status=400)

        # Get values from the request data or use default values
        theme = data['theme'] if 'theme' in data and data['theme'] != '' else '?theme'
        hadith_number = data['hadith_number'] if 'hadith_number' in data and data['hadith_number'] != '' else '?hadith_number'
        versetext = data['versetext'] if 'versetext' in data and data['versetext'] != '' else '?vtext'
        chapterNo = data['chapterNo'] if 'chapterNo' in data and data['chapterNo'] != '' else '?chapterNo'
        verseNo = data['verseNo'] if 'verseNo' in data and data['verseNo'] != '' else '?verseNo'
        mentions = data['mentions'] if 'mentions' in data and data['mentions'] != '' else '?mentions'
        subtheme = data['subtheme'] if 'subtheme' in data and data['subtheme'] != '' else '?subtheme'
        RootNarrator = data['RootNarrator'] if 'RootNarrator' in data and data['RootNarrator'] != '' else '?root_narrator'
        narrator = data['narrators'][0]['name'] if 'narrators' in data and data['narrators'] and data['narrators'][0].get('name') != '' else '?narrator'
        narratortitle = data['narrators'][0]['title'] if 'narrators' in data and data['narrators'] and data['narrators'][0].get('title') != '' else 'narrator-title'
        applyLimit = data.get('applyLimit', True)
        limit = data.get('limit', '')

        query = constructHadithSparQLQueryString_fullgraph(
            theme=theme, mentions=mentions, hadith_number=hadith_number,
            narrator=narrator, narratortitle=narratortitle,
            applyLimit=applyLimit, limit=limit
        )
      
        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query)
        print(query)
        result = Sparql_Endpoint(get_query, prefix)
        print("Theme selected is:", theme)
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'})

@csrf_exempt
def query_hadith(request):
    print('backend/POST')
    print(request.body)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request body'}, status=400)

        # Get values from the request data or use default values
        theme = data['theme'] if 'theme' in data and data['theme'] != '' else '?theme'
        hadith_number = data['hadith_number'] if 'hadith_number' in data and data['hadith_number'] != '' else '?hadith_number'
        versetext = data['versetext'] if 'versetext' in data and data['versetext'] != '' else '?vtext'
        chapterNo = data['chapterNo'] if 'chapterNo' in data and data['chapterNo'] != '' else '?chapterNo'
        verseNo = data['verseNo'] if 'verseNo' in data and data['verseNo'] != '' else '?verseNo'
        mentions = data['mentions'] if 'mentions' in data and data['mentions'] != '' else '?mentions'
        subtheme = data['subtheme'] if 'subtheme' in data and data['subtheme'] != '' else '?subtheme'
        RootNarrator = data['RootNarrator'] if 'RootNarrator' in data and data['RootNarrator'] != '' else '?root_narrator'
        narrator = data['narrators'][0]['name'] if 'narrators' in data and data['narrators'] and data['narrators'][0].get('name') != '' else '?narrator'
        narratortitle = data['narrators'][0]['title'] if 'narrators' in data and data['narrators'] and data['narrators'][0].get('title') != '' else 'narrator-title'
        applyLimit = data.get('applyLimit', True)
        limit = data.get('limit', '')

        query = constructHadithSparQLQueryString_fullgraph(
            theme=theme, mentions=mentions, hadith_number=hadith_number,
            narrator=narrator, narratortitle=narratortitle,
            applyLimit=applyLimit, limit=limit
        )
      
        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query)
        print(query)
        result = Sparql_Endpoint(get_query, prefix)
        print("Theme selected is:", theme)
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'})

@csrf_exempt
def query_hadith2(request):
    print('backend/POST')
    print(request.body)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request body'}, status=400)

        # Get values from the request data or use default values
        Hadith_IRI = data['Hadith_IRI'] if 'Hadith_IRI' in data and data['Hadith_IRI'] != '' else '?Hadith_IRI'
        applyLimit = data.get('applyLimit', True)
        limit = data.get('limit', '')

        query = constructHadithSparQLQueryString_fullgraph_2(
            HADITH_IRI=Hadith_IRI,
            applyLimit=applyLimit, limit=limit
        )
      
        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query)
        print(query)
        result = Sparql_Endpoint(get_query, prefix)
        query2 = constructHadithSparQLQueryString_fullgraph_3(
            HADITH_IRI=Hadith_IRI,
            applyLimit=applyLimit, limit=limit
        )
      
        prefix2 = "http://www.tafsirtabari.com/ontology"
        get_query2 = urllib.parse.quote(query2)
        print(query2)
        result2 = Sparql_Endpoint(get_query2, prefix2)
        return JsonResponse({'result': result, 'result2': result2})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'})
#Verse
@csrf_exempt
def query_verse(request):
    print('backend/POST')
    print(request.body)
    if request.method == 'POST':  # Change to POST
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request body'}, status=400)

        # Get values from the request data or use default values
        chapterNo = data['chapterNo'] if 'chapterNo' in data and data['chapterNo'] != '' else '?chapterNo'
        verseNo = data['verseNo'] if 'verseNo' in data and data['verseNo'] != '' else '?verseNo'
        
        applyLimit = data.get('applyLimit', True)
        limit = data.get('limit', '')
        
        # print(hadithTheme)
        # print(request.body)
       
        query = constructVerseSparQLQueryString_fullgraph(chapterNo, verseNo, applyLimit, limit)
        
        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query)
        print(query)
        result = Sparql_Endpoint(get_query, prefix)
        # Use your Sparql_Endpoint function to query the endpoint
        
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'})

@csrf_exempt
def query_verse2(request):
    print('backend/POST')
    print(request.body)
    if request.method == 'POST':  # Change to POST
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request body'}, status=400)

        # Get values from the request data or use default values
        Verse_IRI = data['Verse_IRI'] if 'Verse_IRI' in data and data['Verse_IRI'] != '' else '?Verse_IRI'
        theme = data['theme'] if 'theme' in data and data['theme'] != '' else '?theme'
        hadithTheme = data['hadithTheme'] if 'hadithTheme' in data and data['hadithTheme'] != '' else '?hadithTheme'
        reference = data['reference'] if 'reference' in data and data['reference'] != '' else '?reference'
        narrator = data['narrator'] if 'narrator' in data and data['narrator'] and data['narrator'] != '' else '?narrator'
        
        applyLimit = data.get('applyLimit', True)
        limit = data.get('limit', '')
        
        print("Reference is: ",reference)
        print("Narrator is: ",narrator)

        # print(hadithTheme)
        # print(request.body)
        #print(hadithTheme)
        query = constructVerseSparQLQueryString_fullgraph2(Verse_IRI,theme,reference,
                                                 applyLimit, limit)
        
        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query)
        #print(query)
        result = Sparql_Endpoint(get_query, prefix)

        query2 = constructVerseSparQLQueryString_fullgraph3(Verse_IRI,hadithTheme, 
                                                narrator,  applyLimit, limit)
        
        prefix2 = "http://www.tafsirtabari.com/ontology"
        get_query2 = urllib.parse.quote(query2)
        #print(query2)
        result2 = Sparql_Endpoint(get_query2, prefix2)

        #print("Hello this is result 2: ", result2)
        #print("Query for result 2 is: ", query2)
        query3 = constructVerseSparQLQueryString_fullgraph4(Verse_IRI,applyLimit, limit)
        
        prefix3 = "http://www.tafsirtabari.com/ontology"
        get_query3 = urllib.parse.quote(query3)
        #print(query3)
        result3 = Sparql_Endpoint(get_query3, prefix3)

        query4 = constructVerseSparQLQueryString_fullgraph5(Verse_IRI, applyLimit, limit)
        
        prefix4 = "http://www.tafsirtabari.com/ontology"
        get_query4 = urllib.parse.quote(query4)
        #print(query4)
        result4 = Sparql_Endpoint(get_query4, prefix4)
        # Use your Sparql_Endpoint function to query the endpoint
        
        return JsonResponse({'result': result, 'result2': result2, 'result3': result3, 'result4': result4})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'})



#commentary
@csrf_exempt
def query_commentary(request):
    print('backend/POST')
    print(request.body)
    if request.method == 'POST':  # Change to POST
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request body'}, status=400)

        # Get values from the request data or use default values
        commno = data['commno'] if 'commno' in data and data['commno'] != '' else '?number'
        chapterNo = data['chapterNo'] if 'chapterNo' in data and data['chapterNo'] != '' else '?chapter_no'
        verseNo = data['verseNo'] if 'verseNo' in data and data['verseNo'] != '' else '?V_no'
        theme = data['theme'] if 'theme' in data and data['theme'] != '' else '?theme'
        mentions = data['mentions'] if 'mentions' in data and data['mentions'] != '' else '?mentions'
        applyLimit = data.get('applyLimit', True)
        limit = data.get('limit', '')
       
        print(theme)
        query = constructCommentarySparQLQueryString_fullgraph(commno, chapterNo, verseNo, theme, mentions,
                                                     applyLimit, limit)
        
        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query)
        #print(query)
        result = Sparql_Endpoint(get_query, prefix)
        # Use your Sparql_Endpoint function to query the endpoint
        
        print(query)

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'})


@csrf_exempt
def query_commentary2(request):
    print('backend/POST')
    print(request.body)
    if request.method == 'POST':  # Change to POST
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request body'}, status=400)

        Commentary_IRI = data['Commentary_IRI'] if 'Commentary_IRI' in data and data['Commentary_IRI'] != '' else '?Commentary_IRI'
        subtheme = data['subtheme'] if 'subtheme' in data and data['subtheme'] != '' else '?subtheme'
        applyLimit = data.get('applyLimit', True)
        limit = data.get('limit', '')
       
        print(subtheme)
        query = constructCommentarySparQLQueryString_fullgraph2(Commentary_IRI, subtheme,
                                                     applyLimit, limit)
        
        #print(query)
        
        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query)
        #print(query)
        result = Sparql_Endpoint(get_query, prefix)

        query2 = constructCommentarySparQLQueryString_fullgraph3(Commentary_IRI,
                                                     applyLimit, limit)
        
        prefix2 = "http://www.tafsirtabari.com/ontology"
        get_query2 = urllib.parse.quote(query2)
        #print(query)
        result2 = Sparql_Endpoint(get_query2, prefix2)
        # Use your Sparql_Endpoint function to query the endpoint
        
        #print(query2)

        print('Result is: ', result)
        print('Query 2 is:', query2)

        return JsonResponse({'result': result , 'result2': result2})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'})


# Federated Query
@csrf_exempt
def query_federated(request):
    print('backend/POST')
    print(request.body)
    if request.method == 'POST':  # Change to POST
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request body'}, status=400)

        # Get values from the request data or use default values
        person = data['person'] if 'person' in data and data['person'] != '' else '?person'
        applyLimit = data.get('applyLimit', True)
        limit = data.get('limit', '')

        query = FederatedQuery(person, applyLimit, limit)
        
        prefix = "http://www.tafsirtabari.com/ontology"  # Change this as needed
        get_query = urllib.parse.quote(query)
        print(query)
        result = Sparql_Endpoint(get_query, prefix)
        # Use your Sparql_Endpoint function to query the endpoint
        
        abstracts = []
        for results in result["results"]["bindings"]:
            abstract = results["abstract"]["value"]
            abstracts.append(abstract)
        
            if abstract:
                return JsonResponse({'result': result})
        # Check if abstracts are empty
        if not abstracts:
            # If abstracts are empty, do something
            print("Abstracts are empty")
            query = FederatedQuery1_2(person, applyLimit, limit)
        
            prefix = "http://www.tafsirtabari.com/ontology"  # Change this as needed
            get_query = urllib.parse.quote(query)
            print(query)
            result = Sparql_Endpoint(get_query, prefix)
            for results in result["results"]["bindings"]:
                abstract = results["abstract"]["value"]
                abstracts.append(abstract)

            if not abstracts:
                # If abstracts are empty, do something
                print("Abstracts are empty")
                query = FederatedQuery1_3(person, applyLimit, limit)
            
                prefix = "http://www.tafsirtabari.com/ontology"  # Change this as needed
                get_query = urllib.parse.quote(query)
                print(query)
                result = Sparql_Endpoint(get_query, prefix)
            # Check if abstracts are empty
                return JsonResponse({'result': result})
            else:
                # If abstracts are not empty, do something else
                print("Abstracts are not empty")
                return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'})

#Competency Question 1
@csrf_exempt
def competency_question1(request):
    if request.method == 'GET':
        # Use the SPARQL query from the function
        query_string = competencyquestion1()

        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query_string)
        result = Sparql_Endpoint(get_query, prefix)

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})
    

# chain of narrators
@csrf_exempt
def chain_narrators(request):
    print('From chain narrators')
    print(request.body)
    if request.method == 'POST':  # Change to POST
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request body'}, status=400)

        # Get values from the request data or use default values
        hadithNo = data['hadithNo'] if 'hadithNo' in data and data['hadithNo'] != '' else '?hadithNo'
        applyLimit = data.get('applyLimit', True)
        limit = data.get('limit', '')

        query = getNarratorChain(hadithNo,applyLimit, limit)
        
        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query)
        #print(query)
        result = Sparql_Endpoint(get_query, prefix)
        #print(result)
        # Use your Sparql_Endpoint function to query the endpoint
        
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'})


@csrf_exempt
def query_federated2(request):
    print('backend/POST')
    print(request.body)
    if request.method == 'POST':  # Change to POST
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request body'}, status=400)

        # Get values from the request data or use default values
        information = data['information'] if 'information' in data and data['information'] != '' else 'information'
        applyLimit = data.get('applyLimit', True)
        limit = data.get('limit', '')

        query = FederatedQuery_2(information, applyLimit, limit)
        
        prefix = "http://www.tafsirtabari.com/ontology"  # Change this as needed
        get_query = urllib.parse.quote(query)
        print(query)
        result = Sparql_Endpoint(get_query, prefix)

        print("Result is: ", result)
        # Use your Sparql_Endpoint function to query the endpoint
        abstracts = []
        for results in result["results"]["bindings"]:
            abstract = results["abstract"]["value"]
            abstracts.append(abstract)
        # Check if abstracts are empty
        if not abstracts:
            # If abstracts are empty, do something
            print("Abstracts are empty")
            query = FederatedQuery_3(information, applyLimit, limit)
        
            prefix = "http://www.tafsirtabari.com/ontology"  # Change this as needed
            get_query = urllib.parse.quote(query)
            print(query)
            result = Sparql_Endpoint(get_query, prefix)

            print("Result is: ", result)
            return JsonResponse({'result': result})
        else:
            # If abstracts are not empty, do something else
            print("Abstracts are not empty")
            return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'})


# Competency Question 2
@csrf_exempt
def competency_question2(request):
    if request.method == 'GET':
        query_string = competencyquestion2()

        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query_string)
        result = Sparql_Endpoint(get_query, prefix)

        print({"Result is: ": result})
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})

# Competency Question 3
@csrf_exempt
def competency_question3(request):
    if request.method == 'GET':
        query_string = competencyquestion3()

        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query_string)
        result = Sparql_Endpoint(get_query, prefix)

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})

# Competency Question 4
@csrf_exempt
def competency_question4(request):
    if request.method == 'GET':
        query_string = competencyquestion4()

        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query_string)
        result = Sparql_Endpoint(get_query, prefix)

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})

# Competency Question 5
@csrf_exempt
def competency_question5(request):
    if request.method == 'GET':
        query_string = competencyquestion5()

        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query_string)
        result = Sparql_Endpoint(get_query, prefix)

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})

# Competency Question 6
@csrf_exempt
def competency_question6(request):
    if request.method == 'GET':
        query_string = competencyquestion6()

        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query_string)
        result = Sparql_Endpoint(get_query, prefix)

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})
    
# Competency Question 7
@csrf_exempt
def competency_question7(request):
    if request.method == 'GET':
        query_string = competencyquestion7()

        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query_string)
        result = Sparql_Endpoint(get_query, prefix)

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})
    
# Competency Question 8
@csrf_exempt
def competency_question8(request):
    if request.method == 'GET':
        query_string = competencyquestion8()

        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query_string)
        result = Sparql_Endpoint(get_query, prefix)

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})
    
# Competency Question 9
@csrf_exempt
def competency_question9(request):
    if request.method == 'GET':
        query_string = competencyquestion9()

        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query_string)
        result = Sparql_Endpoint(get_query, prefix)

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})
    
# Competency Question 10
@csrf_exempt
def competency_question10(request):
    if request.method == 'GET':
        query_string = competencyquestion10()

        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query_string)
        result = Sparql_Endpoint(get_query, prefix)

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})
    
# Competency Question 11
@csrf_exempt
def competency_question11(request):
    if request.method == 'GET':
        query_string = competencyquestion11()

        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query_string)
        result = Sparql_Endpoint(get_query, prefix)

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})
    
# Competency Question 12
@csrf_exempt
def competency_question12(request):
    if request.method == 'GET':
        query_string = competencyquestion12()

        prefix = "http://www.tafsirtabari.com/ontology"
        get_query = urllib.parse.quote(query_string)
        result = Sparql_Endpoint(get_query, prefix)

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})