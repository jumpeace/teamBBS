import sendMsg from '../base.js';

const create = () => {
    form = $('#create_display > form')
    form_items = {
        content: form.find('[name=new_content')
    }
    
    form.submit(event => {
        event.preventDefault();

        $.ajax({
            type: form.prop('method'),
            url: form.prop('action'),
            data: form.serialize(),
            dataType: 'text'
        })
        .done((response, textStatus, jqXHR) => {
            const objectResponse = JSON.parse(response)
            $('#list_display').append(`<a href="${$('#url').text()}${objectResponse.id}/">${objectResponse.content}</a>`);
            sendMsg.done(jqXHR.status, textStatus, '投稿を作成しました。');
            console.log(`Created post. ${jqXHR.status}`)
            // http404表示リセット
            $('#http404').text('');
            // 入力欄リセット
            form_items['new_content'].val('');
        })
        .fail((jqXHR, textStatus) => {
            sendMsg.fail(jqXHR.status, textStatus, '投稿できませんでした。');
            alert(`投稿できませんでした（Status Code: ${jqXHR.status}）`);
        });
        return false;
    })
}

$(document).ready(() => {
    create();
});
