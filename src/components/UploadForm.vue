<template>
    <form @submit.prevent="uploadPhoto" class="d-flex flex-column justify-content-center">
        <div class="form-group">
            <label for="description">Description</label>
            <input type="text" class="form-control" id="description" v-model="description" />
        </div>
        <div class="form-group">
            <label for="photo">Photo</label>
            <div></div>
            <input type="file" class="form-control-file" id="photo"/>
            <div class="form-group">
                <button type="submit" class="btn btn-primary">Upload</button>
            </div>
        </div>
    </form>
</template>


<script>
export default {
    data() {
        return {
            csfr_token: ''
        }
    },
    methods: {
        created() {
            this.data.csfr_token();
        },

        uploadPhoto() {
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);

            fetch("/api/upload", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRF-TOKEN': this.csfr_token
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

        getCsfrToken(){
            let self = this;
            fetch("/api/csrf-token")
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                console.log(data);
                self.csrfToken = data.csfr_token;
            })
        }
    },
};

</script>