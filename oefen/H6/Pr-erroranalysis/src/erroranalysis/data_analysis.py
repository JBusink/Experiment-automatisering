from erroranalysis.error_equations import error_multiplicate
import click

# results in meters of measuring kitchen table

@click.command()
@click.option("-l","--table_length",default = 1,help = "Lenght of table",type=float ,show_default=True,)
@click.option("-w","--table_width",default = 1.,help = "width of table", show_default=True,)
@click.option("-we","--table_width_err",default = 0.,help = "error width of table", show_default=True,)
@click.option("-le","--table_length_err",default = 0.,help = "error length of table", show_default=True,)
def test_table(table_length,table_width,table_width_err,table_length_err):
    print(table_length)
    area_table, area_table_err = error_multiplicate(table_length, table_length_err, table_width, table_width_err)
    print(f"Area of the kitchen table is: {area_table:.4f} \u00B1 {area_table_err:.4f} m")


test_table()
if __name__ == "__main__":
    test_table()