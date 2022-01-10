
const modalBtn = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn  = document.getElementById('start-button')
const url = window.location.href
modalBtn.forEach(modalBtn=>modalBtn.addEventListener('click',()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-name')
    const numquestions = modalBtn.getAttribute('data-questions')
    const time = modalBtn.getAttribute('data-time')
    const pass = modalBtn.getAttribute('data-pass')
    modalBody.innerHTML =`<div class="h5 mb-3">Boshlaysizmi:<b>${name}</b></div>
    <div class="text-muted">
        <ul>
            <li>Test soni:<b>${numquestions}</b></li>
             <li>Test vaqti:<b>${time}</b></li>
        </ul>
        </div>`
startBtn.addEventListener('click',()=>{
    window.location.href = url + pk
})
}))