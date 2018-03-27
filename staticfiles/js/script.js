$(document).ready(main);

function main() {
    // All the script goes here



    $('#contactForm').formValidation({
        framework: 'bootstrap',
        icon : {
            valid : 'glyphicon glyphicon-ok',
            invalid : 'glyphicon glyphicon-remove',
            validating : 'glyphicon glyphicon-refresh',
        },
        fields: {
            name: {
                validators: {
                    notEmpty: {
                        message: 'Name is required'
                    },
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'Email is required'
                    },
                    emailAddress: {
                        message: 'The input is not a valid email address'
                    }
                }
            },
            subject: {
                validators: {
                    notEmpty: {
                        message: 'Subject helps me organize'
                    },
                }
            },
            message: {
                validators: {
                    notEmpty: {
                        message: 'Your message is valued and required'
                    },
                }
            },
        }
    })

}
