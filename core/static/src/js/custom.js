$(document).ready(function(){
    

    $('#update_form').submit(function(){
        data = {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"').val(),
            'inputName': $('#inputName').val(),
            'inputJob': $('#inputJob').val(),
            'inputLocation': $('#inputLocation').val(),
            'inputEducation': $('#inputEducation').val(),
            'inputSkills': $('#inputSkills').val(),
            'inputExperience': $('#inputExperience').val(),
        }

        $.ajax({
            url: 'update_profile',
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            success: function(response){
                console.log(response)
                if (response){
                    alert('Update Success!');
                    $('#agree').prop('checked', false);
                    check_agrre_termsand_conditions();
                    activaTab('activity');
                    $('#new_active').prepend()
                }
            },
        });
        event.preventDefault();
    })


    function check_agrre_termsand_conditions(){
        if ($('#agree').prop('checked')){
            $('#submit').prop('disabled', false)
        } else {
            $('#submit').prop('disabled', true)
        }
    }
    check_agrre_termsand_conditions()
    $('#agree').click(function(){
        check_agrre_termsand_conditions()
    })

    function activaTab(tab){
        $('.nav-link a[href="#' + tab + '"]').tab('show');
    };
})