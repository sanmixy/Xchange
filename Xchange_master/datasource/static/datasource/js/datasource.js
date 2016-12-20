/**
 * Created by Administrator on 16-12-15.
 */

$(function () {
    function bind_events() {
        $('button#add_datasource_hook').click(function () {
            $('div#datasource_add_modal').modal('show');
        });

        $('button#add_datasource').click(function () {
            var post_data = {
                'alias': $('input#alias').val().trim(),
                'department': $('select#departments').val().trim(),
                'system': $('select#systems').val().trim(),
                'type': $('select#source_types').val().trim(),
                'database_type': $('select#database_types').val().trim(),
                'host_active': $('input#host_active').val().trim(),
                'port_active': $('input#port_active').val().trim(),
                'database_name': $('input#database_name').val().trim(),
                'username': $('input#username').val().trim(),
                'passcode': $('input#passcode').val().trim()
            };
            sender('/datasource/push', process_push_datasource_result, post_data);
            function process_push_datasource_result(r) {
                if (r.result) {
                    alert('yes');
                    $('div#datasource_add_modal').modal('hide');
                } else {
                    alert('no');
                }
            }
        });

        $('div#datasource_add_modal').on('shown.bs.modal', function () {
            init_dept_and_system_combobox();
        });

        $('select#departments').change(function () {
            var selected_dept = $('select#departments').val();
            if (!_.isEmpty(selected_dept))
                sender('/datasource/system/filter', process_system_data, {'department': selected_dept})
        });

        function init_dept_and_system_combobox() {
            sender('/datasource/department/all', process_dept_data, null);
        }
    }

    function process_dept_data(r) {
        if (r.result) {
            var $departments = $('select#departments');
            $departments.empty().append(JSON.parse(r.data).map(function (_) {
                //noinspection JSUnresolvedVariable
                return '<option value="' + _.pk + '">' + _.fields.department_name + '</option>';
            }).join(''));

            var default_pk = $departments.val();
            if (!_.isEmpty(default_pk)) {
                sender('/datasource/system/filter', process_system_data, {'department': default_pk});
            }
        }
    }

    function process_system_data(r) {
        if (r.result) {
            var $systems = $('select#systems');
            $systems.empty().append(JSON.parse(r.data).map(function (_) {
                //noinspection JSUnresolvedVariable
                return '<option value="' + _.pk + '">' + _.fields.system_name + '</option>';
            }));
        }
    }

    bind_events();
    draw_datasource_table();
});

function draw_datasource_table() {
    $('table#datasource').bootstrapTable({});
}