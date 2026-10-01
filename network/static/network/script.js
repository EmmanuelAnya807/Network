document.addEventListener("DOMContentLoaded", function () {
    console.log("Javascript loaded.")
    const edit_buttons = document.querySelectorAll(".edit-post");
    const save_buttons = document.querySelectorAll(".save-post");
    const like_buttons = document.querySelectorAll(".like-post")

    edit_buttons.forEach((button) => {
        button.addEventListener('click', (event) => {

            event.preventDefault()

            console.log("Edit clicked.")

            button.style.display = 'none'

            const post_id = button.dataset.postId;
            const post_to_edit = document.querySelector(`#post-content-${post_id}`);
            const current_content = post_to_edit.textContent;
            const edit_area = document.createElement("textarea");
            const save_post = document.querySelector(`.save-post[data-post-id="${post_id}"]`)

            edit_area.value = current_content;
            edit_area.id = `post-content-${post_id}`;
            edit_area.className = "form-control"
            post_to_edit.replaceWith(edit_area);

            save_post.classList.remove('d-none')
        })
    })

    save_buttons.forEach((button) => {
        button.addEventListener('click', (event) => {

            event.preventDefault()

            console.log("Save clicked.")

            const post_id = button.dataset.postId;
            const post_to_save = document.querySelector(`#post-content-${post_id}`);
            const current_content = post_to_save.value;
            const content = {
                    content: current_content
                }
            const csrftoken = document.cookie
                .split(';')
                .find(cookie => cookie.trim().startsWith("csrftoken="))
                .replace("csrftoken=", "")

            const existing_error = document.querySelector(".edit-error")

            if (current_content.trim() === '') {
                if (!existing_error) {

                    const error_message = document.createElement('p')
                    error_message.textContent = "This field cannot be left blank."
                    error_message.className = 'text-danger edit-error'
                    post_to_save.after(error_message)
                    return
                }
            }
            else {
                if (existing_error) {
                    existing_error.remove()
                }
                console.log("About to send edit request.")

                fetch(`/edit_post/${post_id}`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrftoken
                    },
                    body: JSON.stringify(content)
                })
                .then(async response => {
                    console.log("Response status:", response.status)
                    console.log(response.ok)

                    if (!response.ok) {
                        const errorData = await response.json()
                        const errorMessage = errorData.error

                        throw new Error(errorMessage)
                    }
                    return response.json()
                })
                .then(data => {
                    console.log(data)

                    button.style.display = 'none'

                    const edited_content = document.createElement('p')
                    const edit_post = document.querySelector(`.edit-post[data-post-id="${post_id}"]`)

                    edited_content.textContent = current_content
                    edited_content.id = `post-content-${post_id}`
                    edited_content.className = 'article-content'
                    post_to_save.replaceWith(edited_content)
                    edit_post.style.display = 'block'

                })
                .catch(error => {
                    console.log("Django error:", error.message)
                    showUiError(error.message, post_to_save)
                })
            }
        })
    })
    like_buttons.forEach(button => {
        button.addEventListener('click', () => {
            console.log("like clicked")

            const post_liked = button.dataset.postId
            const csrftoken = document.cookie
                .split(';')
                .find(cookie => cookie.trim().startsWith("csrftoken="))
                .replace("csrftoken=", "")
            console.log(post_liked)

            fetch(`/like/${post_liked}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken
                }
            })
            .then(response => {
                console.log(response)
                if (response.redirected) {
                    window.location.replace(response.url)
                }
                else {
                    return response.json()
                    .then(data => {

                        if (data.status === 'liked') {
                            button.classList.remove('bi-heart')
                            button.classList.add('bi-heart-fill')
                        }
                        else {
                            button.classList.remove('bi-heart-fill')
                            button.classList.add('bi-heart')
                        }
                        const like_count = document.querySelector(`.like-count[data-post-id="${post_liked}"]`)
                        like_count.textContent = data.count
                        console.log(data)
                    })
                }
            })
        })
    })

});


function showUiError(message, post_to_save) {
    const error_message = document.createElement('p')
    error_message.textContent = message
    error_message.className = 'text-danger edit-error'
    post_to_save.after(error_message)
}


