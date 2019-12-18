function world()
{
    let trigger = 0
    if (trigger == 0){
        let fuck1 = document.getElementById("fuck1")
        let fuck2 = document.getElementById("fuck2")
        let fuck3 = document.getElementById("fuck3")
        let fuck4 = document.getElementById("fuck4")
        fuck1.innerHTML = 'Hello World!'
        fuck2.innerHTML = 'Hello World!'
        fuck3.innerHTML = 'Hello World!'
        fuck4.innerHTML = 'Hello World!'
        trigger++
        button.innerHTML = 'swear.ON'

    }
    else{
        let button = document.getElementById("button1")
        let fuck1 = document.getElementById("fuck1")
        let fuck2 = document.getElementById("fuck2")
        let fuck3 = document.getElementById("fuck3")
        let fuck4 = document.getElementById("fuck4")
        fuck1.innerHTML = 'Hello Fucking World!'
        fuck2.innerHTML = 'Hello Fucking World!'
        fuck3.innerHTML = 'Hello Fucking World!'
        fuck4.innerHTML = 'Hello Fucking World!'
        button.innerHTML = 'no swear'
        trigger--
    }
    
}