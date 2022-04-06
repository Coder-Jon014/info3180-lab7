<template>
    <form
        @submit.prevent="uploadPhoto" id="uploadForm" method="POST" enctype="multipart/form-data">
        <div class="form-group">
            <label for="photo">Select a Photo to Upload</label>
            <div></div>
            <input type="file" class="form-control-file" id="photo" name="photo" required>
        </div>
        <div class="form-group">
            <label for="description">Description</label>
            <textarea class="form-control" id="description" name="description" rows="3" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Upload</button>
    </form>
</template>


<script>
export default {
    data() {
        return {csrfToken: ''}
    },
    created() {
        this.getCsfrToken();
    },
    methods: {
        uploadPhoto() {
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);

            fetch("/api/upload", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRF-TOKEN': this.csrfToken
                }

            })
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {
                    // display a success message
                    console.log(data);
                })
                .catch(function (error) {
                    console.log(error);
                });
        },

        getCsfrToken() {
            let self = this;
            fetch("/api/csrf-token")
                .then((response) => {
                    return response.json();
                })
                .then((data) => {
                    console.log(data);
                    self.csrfToken = data.csrf_token;
                })
        }
    },
};

</script>