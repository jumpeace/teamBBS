const create = () => {
    const form = $('#create_display > form');
    const form_items = {
        new_user: form.find('[name=new_user]')
    }

    form.submit(event => {
        event.preventDefault();

        if (form_items['new_user'].find('option:selected').val() === form_items['new_user'].data('invalid_val')) {
            return false
        }

        $.ajax({
            type: form.prop('method'),
            url: form.prop('action'),
            data: form.serialize(),
            dataType: 'text'
        })
            // TODO こっちにリダイレクトされない
            .done((response, textStatus, jqXHR) => {
                new_user = JSON.parse(response)['new_user'];
                $('#list_display').append(`<div><input type="checkbox">${new_user['email']}</div>`);
                console.log(`役職にユーザー"${new_user['email']}"を追加しました\n${jqXHR.status}（${textStatus}）`)
                // http404表示リセット
                $('#http404').text('');
                // 入力欄リセット
                form_items['new_user'].find(`option[value=${new_user['id']}]`).remove()
            })
            .fail(jqXHR => {
                alert(`役職にユーザーを追加できませんでした（Status Code: ${jqXHR.status}）`);
            });
        return false;
    })
}

const delete_ = () => {
    const form = $('#delete_display > form');
    const form_items = {
        delete_pks: $('.delete_pk'),
    };

    form_items.delete_pks.forEach(el => console.log(el))

    form.submit(event => {
        event.preventDefault();
        $.ajax({
            type: form.prop('method'),
            url: form.prop('action'),
            data: form.serialize(),
            dataType: 'text',
        })
            .done((response, textStatus, jqXHR) => {
                form_items['delete_pks'].forEach(el => {
                    el.remove();
                })
                console.log(response, textStatus, jqXHR);
            })
            .fail((jqXHR, textStatus) => {
                alert(jqXHR, textStatus);
            })
    })
    return false;
}

$(document).ready(() => {
    create();
    delete_();
});
