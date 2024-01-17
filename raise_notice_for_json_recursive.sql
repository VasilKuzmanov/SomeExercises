CREATE OR REPLACE FUNCTION raise_notice_for_json_recursive(json_input jsonb)
RETURNS VOID AS $$
DECLARE
    key_text text;
    value_text text;
BEGIN

    FOR key_text, value_text IN SELECT * FROM jsonb_each_text(json_input)
    LOOP

        RAISE NOTICE 'Key: %, Value: %', key_text, value_text;

        IF jsonb_typeof(json_input->key_text) = 'object' THEN
            PERFORM raise_notice_for_json_recursive(json_input->key_text);
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;


SELECT raise_notice_for_json_recursive('{"name": "John", "age": "30", "address": {"city": "New York", "zip": "10001"}}');