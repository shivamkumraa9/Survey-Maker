data_element=document.querySelector(".Data")
Question_element=document.querySelector(".QUESTION")
add_question_button=document.getElementById("add_more")
add_question_button.addEventListener("click",add_data)
delete_button=document.createElement("button")
delete_button.setAttribute('onclick',"del(this)")
delete_button.innerText="Delete This Question"
delete_button.classList.add("btn")
delete_button.classList.add("btn-danger")
copy=Question_element.cloneNode(true)
copy.appendChild(delete_button)
counter=1
function create_element(){
    return copy.cloneNode(true);
}

function add_data(){
    counter++
    if (counter>14){
        alert("Max Limit is 15")
    }
    else{
        data_element.appendChild(create_element())
    }
}

function del(s){
    s.parentElement.remove()
    counter --
}
