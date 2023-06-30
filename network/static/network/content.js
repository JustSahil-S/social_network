document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    const likeButton= document.querySelectorAll('.LikeButton');
    likeButton.forEach((button) => {
        button.addEventListener("click", () => LikeCounter(button.id));
        /* button.addEventListener("click", () => RemoveSelection(button.id)); */
    })
    const EditButton = document.querySelectorAll('.EditButtonClass');
    EditButton.forEach((button) => {
        button.addEventListener("click", () => displayForm(button.id));
    })
    const editForm = document.querySelectorAll(".submitForm");
    editForm.forEach((form) => { form.addEventListener('submit', (event)=>Edit(event, form.id))});

    const followButton = document.querySelector('.FollowButton');
    if (followButton) {
        followButton.addEventListener("click", () => FollowCounter(followButton.id));}
      
      
});

function LikeCounter(id) {
    var id_short = id.split('-')[1];
    fetch(`/likePosts/${id_short}`).then(response => response.json()).then(x => {
        var y = document.getElementById(id);
        (y.innerHTML = ` 👍 ${x["likecount"]}`)
        if (y.style.backgroundColor == "white"){
            y.style.backgroundColor = "rgb(33, 199, 33)";
        } else {
            y.style.backgroundColor = "white";
        }
    })
};

function FollowCounter(id) {
    var id_short = id.split('-')[1];
    fetch(`/follow/${id_short}`).then(response => response.json()).then(x => {
        var y = document.getElementById(id);
        (document.getElementById(`followCounter-${id_short}`).innerHTML = ` Followers: ${x["followcount"]}`)
        if (y.style.backgroundColor == "white"){
            y.style.backgroundColor = "rgb(33, 199, 33)";
            y.innerHTML="Following"

        } else {
            y.style.backgroundColor = "white";
            y.innerHTML="Follow"

        }
    })
};


function Edit(event, id) {
    event.stopImmediatePropagation();
    event.preventDefault();
    fetch(`/edit/${id}`, {
        method: 'POST',
        body: JSON.stringify({
          newContent: document.querySelector(`#newContent-${id}`).value
        })
    }).then(() => {
        console.log(document.getElementById(`content-${id}`).innerHTML)
        document.getElementById(`content-${id}`).innerHTML = document.querySelector(`#newContent-${id}`).value;
        document.getElementById(id).style.display = "none"
        document.getElementById(`content-${id}`).style.display = "block"

    })
}


function displayForm(id) {
    var id_short = id.split('-')[1];
    if (document.getElementById(id_short).style.display == "none") {
        document.getElementById(id_short).style.display = "block";
        document.getElementById(`content-${id_short}`).style.display = "none"
    }
    else {
        document.getElementById(id_short).style.display = "none";
        document.getElementById(`content-${id_short}`).style.display = "block"
    }
}

/* function FollowCounter(id) {
    var id_short = id.split('-')[1];
    fetch(`/follow/${id_short}`).then(response => response.json()).then(x => {
        var y = document.getElementById(id);
        (y.innerHTML = ` Followers: ${x["followcount"]}`)
        if (y.style.backgroundColor == "white"){
            y.style.backgroundColor = "rgb(33, 199, 33)";
        } else {
            y.style.backgroundColor = "white";
        }
    })
}; */