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
    const update_content = $('#update_display > form > input:text')
    let before_content;
    $('#display_to_update_btn').on('click', () => {
        change_display('update');
        before_content = update_content.val()
    });

    update_form.submit(event => {
        event.preventDefault();
        if (update_content.val() !== before_content) {
            $.ajax({
                type: update_form.prop('method'),
                url: update_form.prop('action'),
                data: update_form.serialize(),
                dataType: 'text'
            })
                .done((response, textStatus, jqXHR) => {
                    const objectResponse = JSON.parse(response)
                    $('#post_content').text(objectResponse.content);
                    update_content.val(objectResponse.content)
                    console.log(`Updated post. ${jqXHR.status}`)
                })
                .fail(jqXHR => {
                    alert(`投稿を更新できませんでした（Status Code: ${jqXHR.status}）`);
                });
        }

        change_display('detail');
        return false;
    })
});