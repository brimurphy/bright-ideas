let countrySelected = $('#id_default_country').val();
        if(!countrySelected) {
            $('#id_default_country').css('color', '#ced4da');
        }
        $('#id_default_country').change(function() {
            countrySelected = $(this).val();
            if(!countrySelected) {
                $(this).css('color', '#ced4da');
            } else {
                $(this).css('color', '#1f1f1f');
            }
        })