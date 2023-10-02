import os.path
from fpdf import FPDF

Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
image_name = os.path.join(Base_dir, 'reports', 'output', 'logo.jpeg')
analytics_img = os.path.join(Base_dir, 'reports', 'output', 'foo.png')
timeline_image = os.path.join(Base_dir, 'reports', 'output', 'time_line.png')
facebook_logo = os.path.join(Base_dir, 'reports', 'Facebook_f_logo.png')


class PDF(FPDF):
    def __init__(self, predicted_data):
        """
        :param predicted_data: exacted data
        """
        super().__init__()
        self.predicted_data = predicted_data

    def lines(self):
        # Draw outer rectangle
        self.set_fill_color(0, 0.0, 250.0)  # color for outer rectangle
        self.rect(5.0, 5.0, 200.0, 287.0, 'DF')

        # Draw inner rectangle
        self.set_fill_color(255, 255, 255)  # color for inner rectangle
        self.rect(8.0, 8.0, 194.0, 282.0, 'FD')

    def logo(self):

        # Set position for the Facebook logo image (adjust as needed)
        self.image(facebook_logo, x=50, y=15, w=10)

        self.set_xy(163.0, 10.0)
        self.image(image_name, w=1586 / 50, h=1920 / 50)

    def footer(self):
        # Add page number
        self.set_text_color(0, 0, 0)
        self.set_xy(0, -15)
        self.set_font('Arial', '', 16)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_page_with_lines(self):
        self.add_page()
        self.lines()
        self.logo()
        # self.footer()

    def titles(self, title_text):
        self.set_xy(0.0, 0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220, 50, 50)
        self.cell(w=210.0, h=40.0, align='C', txt=title_text, border=0)

    def doc_title(self, document: str, x: int, y: int, x2: int, post_id=None):
        self.set_text_color(0, 0, 0)
        self.set_xy(x , (y- 10))
        self.set_font('Arial', 'B', 12)
        if post_id is not None:
            self.cell(w=210.0, h=40.0, align='l', txt=f"PostId: {post_id}", border=0)
        # Title
        self.set_xy(x, y)
        self.cell(w=210.0, h=40.0, align='l', txt=f"{document}", border=0)
        self.line(x, (y + 22), x2, (y + 22))

    def analytics_detail(self):
        self.set_xy(30.0, 55.0)
        if os.path.exists(analytics_img):
            self.image(analytics_img, w=150)

    def comments_detail(self, best_comments, worst_comments, likes_count, comments_count, share_count):

        # self.set_xy(30.0, 141.0)
        self.set_xy(30.0, 167.0)

        if best_comments is not None:
            self.set_text_color(0, 0, 0)
            self.cell(w=210.0, h=40.0, align='l',
                      txt=f"Best Comment        :  {best_comments}",
                      border=0)

        self.set_xy(30.0, 177.0)
        if worst_comments is not None:
            self.set_text_color(0, 0, 0)
            self.cell(w=210.0, h=40.0, align='l',
                      txt=f"Worst comment       :  {worst_comments} ",
                      border=0)
        self.set_xy(30.0, 187.0)
        self.set_text_color(0, 0, 0)
        self.cell(w=210.0, h=40.0, align='l',
                  txt=f"Engagement      :   {likes_count + comments_count}+",
                  border=0)

        self.set_xy(30.0, 197.0)
        self.set_text_color(0, 0, 0)
        self.cell(w=210.0, h=40.0, align='l',
                  txt=f"Total Comments      :   {comments_count}",
                  border=0)

        self.set_xy(30.0, 207.0)
        self.set_text_color(0, 0, 0)
        self.cell(w=210.0, h=40.0, align='l',
                  txt=f"Total Likes     :   {likes_count}",
                  border=0)

        self.set_xy(30.0, 217.0)
        self.set_text_color(0, 0, 0)
        self.cell(w=210.0, h=40.0, align='l',
                  txt=f"Total Share Count       :   {share_count}",
                  border=0)

    def timeline(self):
        self.set_xy(20.0, 65.0)
        if os.path.exists(timeline_image):
            self.image(timeline_image, w=150)


def main(best_comments, worst_comments, likes_count, comments_count, share_count, post_id):
    pdf = PDF('predicted_data')  # pdf object
    pdf.add_page_with_lines()
    pdf.titles('Social Analytics Report')
    pdf.doc_title('Post Comments Analytics', 70, 30, 122, post_id)
    pdf.analytics_detail()
    pdf.comments_detail(best_comments, worst_comments, likes_count, comments_count, share_count)
    # Second page
    pdf.add_page_with_lines()
    pdf.titles('Last Page')
    pdf.doc_title('Comments Timelines', 70, 40, 115)
    pdf.timeline()
    pdf.set_author('Acidaes solution pvt ltd')
    pdf.output('report.pdf')


#
if __name__ == "__main__":
    pdf = PDF('predicted_data')  # pdf object

    pdf.add_page_with_lines()
    pdf.titles('Social Analytics Report')
    pdf.doc_title('Post Comments Analytics', 70, 30, 122)
    pdf.analytics_detail()
    pdf.comments_detail('hi', 'no', 2, 3, 2)

    # Second page
    pdf.add_page_with_lines()
    pdf.titles('Last Page')
    pdf.doc_title('Comments Timelines', 70, 40, 115)
    pdf.timeline()

    pdf.set_author('Acidaes solution pvt ltd')
    pdf.output('report.pdf')
