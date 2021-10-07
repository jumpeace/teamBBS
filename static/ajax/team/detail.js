const change_display = (to) => {
    const display_dom = {
        detail: $('#detail_display'),
        update: $('#update_display'),
        delete: $('#delete_display'),
    }
    const processList = [
        {
            to: 'update',
            func: () => {
                display_dom.detail.attr('hidden', true);
                display_dom.update.attr('hidden', false);
                display_dom.delete.attr('hidden', true);
                $('#update_display > form > input:text').focus()
            }
        },
        {
            to: 'detail',
            func: () => {
                display_dom.detail.attr('hidden', false);
                display_dom.update.attr('hidden', true);
                display_dom.delete.attr('hidden', false);
            }
        }
    ];
    processList.find(process => process.to == to)?.func()
}

$(document).ready(() => {
    const update_form = $('#update_display > form');
    const update_name = $('#update_display > form > input:text')
    let before_name;
    $('#display_to_update_btn').on('click', () => {
        change_display('update');
        before_content = update_name.val()
    });

    update_form.submit(event => {
        event.preventDefault();
        if (update_name.val() !== before_name) {
            $.ajax({
                type: update_form.prop('method'),
                url: update_form.prop('action'),
                data: update_form.serialize(),
                dataType: 'text'
            })
                .done((response, textStatus, jqXHR) => {
                    const objectResponse = JSON.parse(response)
                    $('#team_name').text(objectResponse.new_name);
                    update_name.val(objectResponse.new_name)
                    console.log(`Updated team name. ${jqXHR.status}`)
                })
                .fail(jqXHR => {
                    alert(`チーム名を変更できませんでした（Status Code: ${jqXHR.status}）`);
                });
        }

        change_display('detail');
        return false;
    });

    $('#delete_display > form').submit(() => {
        if (!confirm('本当に削除しますか？')) {
            return false;
        }
    })
});