from django.shortcuts import HttpResponse

def task_create(request):
    html_response="""
    <h1>Yangi vazifa yaratish</h1>
    <form>
    <label>
      Vazifa nomi:
      <input type="text" id=vazifa name=vazifa/>     
    </label>
    <br><br>
    
    <label>
     Tavsif:
      <style>
       textarea {
                 weight:170px;
                 height:100px;
      </style>
      
     <textarea>
     </textarea>
    </label>
    <br><br>
    
    <label>
     Muddati:
     <input type="date" id=muddat name=muddat/>
     
    </label>
    <br><br>
    
    <label>
     Muhimlik darajasi:
     <select name="daraja" id="daraja">
        <option value="past">Past</option>
        <option value="o'rta">O'rta</option>
        <option value="yuqori">Yuqori</option>
     </select>

    </label>
    <br></br>
    
    
    <button class="button"> Vazifani saqlash </button>
    
    </form>
    
    
    
    
    """
    return HttpResponse(html_response)