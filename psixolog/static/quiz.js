const url = window.location.href
const Btn = document.getElementById('show').style.display = 'none'
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const quizBox = document.getElementById('quiz-box')
const timerBox = document.getElementById('time-box')
let flag = true
var i = 1
function show() {
    const Btn = document.getElementById('show').style.display = 'block'
}
const activateTimer = (time)=>{
        var minutesleft = 0; //give minutes you wish
        var secondsleft = time; // give seconds you wish
        var finishedtext = "Countdown finished!";
        var end1;
        if (localStorage.getItem("end1")) {
            end1 = new Date(localStorage.getItem("end1"));
        } else {
            end1 = new Date();
            end1.setMinutes(end1.getMinutes() + minutesleft);
            end1.setSeconds(end1.getSeconds() + secondsleft);

        }
        var counter = function () {
            var now = new Date();
            var diff = end1 - now;

            diff = new Date(diff);

            var milliseconds = parseInt((diff % 1000) / 100)
            var sec = parseInt((diff / 1000) % 60)
            var mins = parseInt((diff / (1000 * 60)) % 60)
            //var hours = parseInt((diff/(1000*60*60))%24);

            if (mins < 10) {
                mins = "0" + mins;
            }
            if (sec < 10) {
                sec = "0" + sec;
            }
        if(!flag) {
             clearTimeout()
             localStorage.clear();
        }
        else {if (now >= end1) {
                clearTimeout(interval);
                localStorage.removeItem("end1");
                localStorage.clear();
                if (confirm("TIME UP!")){
                    alert("Vaqt tugadi")
                    sendData()
                }

            } else {
                var value = mins + ":" + sec;
                localStorage.setItem("end1", end1);
                timerBox.innerHTML = `<b>${value}</b>`;
            }
//            save()



        }

        }
        var interval = setInterval(counter, 1000);

}

//function save() {
//	var checkbox = document.getElementById("${questions}-${answer}");
//    localStorage.setItem("${questions}-${answer}", checkbox.checked);
//}
 $.ajax({
                type: "GET",
                url: `${url}data`,
                success: function(response) {
                    const o = 1
                    let data = response.data
                    data.forEach( el=>{
                        for ( const[questions,answers] of Object.entries(el)){
                            quizBox.innerHTML += `
                                <hr>
                                <div class="ml-3 px-5 py-3"> <b>${i}.</b>
                                    <b>${questions}</b>
                                </div>
                            `
                            i++
                            answers.forEach( answer=>{
                                quizBox.innerHTML+=`
                                    <div class="ml-3 px-5">
                                            <input type="radio" id="${questions}-${answer}" class="ans" name="${questions}" value='${answer}'>
                                        <label for="${questions}-${answer}">${answer}</label>
                                    </div>
                                `

                            })

                            }

                            });

                                 activateTimer(response.time)



                },
                error: function(error) {
                    alert('sasa');
                }
            })
let boxes = document.getElementsByClassName('ans').length;


const quizForm = document.getElementById('quiz-form')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    quizForm.style.display = 'none'
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if(el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })

    $.ajax({
        type:'POST',
        url:`${url}save/`,
        data: data,
        success: function(response){
            const results = response.results
            quizForm.classList.add('not-visible')
//            scoreBox.innerHTML+=`<h3><b>Sizning natijangiz:</b> ${response.natija}%</h3>`
            resultBox.innerHTML = `<h3><p class="text-center">${response.pol}</p></h3>`
            results.forEach(res=>{
                const resDiv = document.createElement("div")
                for ( const [question,resp] of Object.entries(res)){
                    resDiv.innerHTML += `<div class="px-5"><b>${question}</b></div>`
                    const cls = ['container','px-5','text-light','h4']
//                    resDiv.classList.add(...cls)

                    if (resp === 'not answered'){
                        resDiv.innerHTML+=`<div class="alert alert-danger px-5" role="alert">
                                                Javob berilmagan!
                                           </div>`
//                        resDiv.classList.add('alert alert-danger')
                    }
                    else {

                        const answer = resp['answered']
                        const correct = resp['correct_answer']



                        if (answer===correct){
//                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML+=`<div class="alert alert-success" role="alert">
                                                    ${answer}
                                                </div>`

                        }
                        else{

//                               resDiv.classList.add('bg-danger')
                               resDiv.innerHTML+=`<div class="alert alert-danger" role="alert">
                                    togri javob:${correct},Tanlangan javob:${answer}</div>  `
                        }

                    }

                }

//                const body = document.getElementsByTagName('BODY')[0]

                resultBox.append(resDiv)
            })


        },
        error:function(error){
            console.log(error)
        }

    })

}
quizForm.addEventListener('submit',e=>{
    e.preventDefault()
    sendData()
    flag = false;
    show()
})





