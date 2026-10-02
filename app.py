import gradio as gr

from gold_cut_off_grade_calculator import calculate_cut_off_grade, format_results_html


def run_calculator(total_cost, gold_price, recovery):
    result = calculate_cut_off_grade(total_cost, gold_price, recovery)
    return format_results_html(result)


with gr.Blocks(title="Gold Cut-off Grade Calculator") as demo:
    gr.Markdown("# Gold Cut-off Grade Calculator")
    gr.Markdown(
        "Enter positive operating cost, gold price, and recovery between 0 and 100 "
        "to compute the gold cut-off grade."
    )

    with gr.Row():
        with gr.Column(scale=1):
            total_cost = gr.Number(
                label="Total operating cost (USD per tonne of ore)",
                value=100.0,
                precision=2,
            )
            gold_price = gr.Number(
                label="Gold price (USD per troy ounce)",
                value=2000.0,
                precision=2,
            )
            recovery = gr.Number(
                label="Recovery (%)",
                value=90.0,
                precision=1,
            )
            calculate_button = gr.Button("Calculate cut-off grade", variant="primary")

        with gr.Column(scale=2):
            result_output = gr.HTML(
                value=format_results_html(
                    calculate_cut_off_grade(100.0, 2000.0, 90.0)
                )
            )

    calculate_button.click(
        fn=run_calculator,
        inputs=[total_cost, gold_price, recovery],
        outputs=result_output,
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
