from sqlalchemy.dialects.postgresql import JSONB
import sqlalchemy as sa

b_id = {
  "name": "b_id",
  "type_": sa.BigInteger,
  "primary_key": True,
  "auto_increment": True,
}

b_key = {
  "name": "b_key",
  "type_": sa.Text,
}

b_hash = {
  "name": "b_hash",
  "type_": sa.Text,
  "index": True,
}

b_source_key = {
  "name": "source_key",
  "type_": sa.Text,
  "index": True,
}

b_source_value = {
  "name": "source_value",
  "type_": sa.Text,
  "index": True,
}

b_is_valid = {
  "name": "is_valid",
  "type_": sa.Boolean,
  "index": True,
}

b_name = {
  "name": "name",
  "type_": sa.Text,
}

b_title = {
  "name": "title",
  "type_": sa.Text,
}

b_summary = {
  "name": "summary",
  "type_": sa.Text,
}

b_options = {
  "name": "options",
  "type_": JSONB,
}

b_labels = {
  "name": "labels",
  "type_": JSONB,
}

b_created_by = {
  "name": "created_by",
  "type_": sa.Text,
}

b_created_ts = {
  "name": "created_ts",
  "type_": sa.DateTime,
}

b_touched_by = {
  "name": "touched_by",
  "type_": sa.Text,
}

b_touched_ts = {
  "name": "touched_ts",
  "type_": sa.DateTime,
}

reference_column_list - [
  b_id,
  b_key,
  b_name,
  b_title,
  b_summary,
  b_is_valid,
  b_options,
  b_labels,
  b_created_by,
  b_created_ts,
]
