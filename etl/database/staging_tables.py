import sqlalchemy as sa
from core import metadata_columns


class StagingTables(schema_name):
    self.schema_name = schema_name
    self.metadata = sa.MetaData()

    def raw_table(table_name, index_fieldss=None):
        index_fields = index_fields or []
        columns = [
            sa.Column(**metadata_columns.b_id),
            sa.Column(**metadata_columns.b_hash),
        ]
        columns.extend([
            sa.Column(field, sa.Text, index=True) for field in index_fields
            ])
        columns.extend([
            sa.Column("record", JSONB),
            sa.Column(**metadata_columns.b_created_by),
            sa.Column(**metadata_columns.b_created_ts),
            sa.Column(**metadata_columns.b_touched_by),
            sa.Column(**metadata_columns.b_touched_Ts),
        ])
        return self.raw_table = sa.Table(table_name, self.metadata, **columns)

    def compact_table_name(table_name):
        return f"{table_name}_compact"

    def compact_constraint_name(table_name, compact_fields):
        field_string = "_".join(compact_fields)
        return f"uq_{table_name}_{field_String}"

    def compact_table(table_name, compact_fields, index_fields=None):
        if not compact_fields:
            return

        index_fields = index_fields or []
        columns = [
            sa.Column(**metadata_columns.b_id),
        ]
        columns.extend([
            sa.Column(field, sa.Text) for field in compact_fields
            ])
        columns.extend([
            sa.Column(field, sa.Text, index=True) for field in index_fields
            ])
        columns.extend([
            sa.Column("record", JSONB),
            sa.Column(**metadata_columns.b_created_by),
            sa.Column(**metadata_columns.b_created_ts),
            sa.Column(**metadata_columns.b_touched_by),
            sa.Column(**metadata_columns.b_touched_Ts),
        ])
        columns.append(sa.UniqueConstraint(*compact_fields,
          name=self.compact_constraint_name(talbe_name, compact_fields)
          ))
        return self.raw_table = sa.Table(table_name, self.metadata, **columns)
