import matplotlib.pyplot as plt
import matplotlib as mpl

# ---------------------------------------------------------
# Font: Times New Roman + Bold
# ---------------------------------------------------------
mpl.rcParams["font.family"] = "Times New Roman"
mpl.rcParams["font.serif"] = ["Times New Roman"]

# Make all default text bold
mpl.rcParams["font.weight"] = "bold"
mpl.rcParams["axes.labelweight"] = "bold"
mpl.rcParams["axes.titleweight"] = "bold"

# ---------------------------------------------------------
# Data
# ---------------------------------------------------------
HOMO = [-5.611, -5.485, -6.132, -5.068, -5.631,
        -5.394, -6.472, -4.742, -5.807]

LUMO = [-1.608, -1.659, -2.736, -1.469, -2.544,
        -1.923, -3.722, -1.562, -3.318]

# HOMO-LUMO gaps
gaps = [LUMO[i] - HOMO[i] for i in range(len(HOMO))]

# ---------------------------------------------------------
# X and Y substituent labels
# ---------------------------------------------------------
X_labels = [
    "H",
    "OH",
    "OH",
    r"NH$_2$",
    r"NH$_2$",
    "OH",
    "OH",
    r"NH$_2$",
    r"NH$_2$"
]

Y_labels = [
    "H",
    "F",
    "CN",
    "F",
    "CN",
    "F",
    "CN",
    "F",
    "CN"
]

# ---------------------------------------------------------
# Figure
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(15, 7))

# Horizontal spacing
spacing = 3.0

# ---------------------------------------------------------
# Plot energy levels
# ---------------------------------------------------------
for i in range(len(HOMO)):

    x = i * spacing

    # -----------------------------------------------------
    # HOMO level - RED SOLID
    # -----------------------------------------------------
    ax.hlines(
        HOMO[i],
        x - 0.45,
        x + 0.45,
        color="red",
        linewidth=2.5,
        label="HOMO" if i == 0 else ""
    )

    # -----------------------------------------------------
    # LUMO level - GREEN SOLID
    # -----------------------------------------------------
    ax.hlines(
        LUMO[i],
        x - 0.45,
        x + 0.45,
        color="green",
        linewidth=2.5,
        label="LUMO" if i == 0 else ""
    )

    # -----------------------------------------------------
    # HOMO-LUMO vertical arrow
    # -----------------------------------------------------
    ax.annotate(
        "",
        xy=(x, LUMO[i] - 0.03),
        xytext=(x, HOMO[i] + 0.03),
        arrowprops=dict(
            arrowstyle="<->",
            linewidth=1.3,
            color="black"
        )
    )

    # -----------------------------------------------------
    # HOMO-LUMO gap
    # -----------------------------------------------------
    ax.text(
        x + 0.15,
        (HOMO[i] + LUMO[i]) / 2,
        f"{gaps[i]:.2f}",
        fontsize=12,
        fontweight="bold",
        va="center",
        ha="left"
    )

    # -----------------------------------------------------
    # X label
    # -----------------------------------------------------
    ax.text(
        x,
        -7.65,
        X_labels[i],
        ha="center",
        va="top",
        fontsize=14,
        fontweight="bold"
    )

    # -----------------------------------------------------
    # Y label
    # -----------------------------------------------------
    ax.text(
        x,
        -8.20,
        Y_labels[i],
        ha="center",
        va="top",
        fontsize=14,
        fontweight="bold"
    )

# ---------------------------------------------------------
# X = and Y = labels
# ---------------------------------------------------------
ax.text(
    -1.05,
    -7.65,
    r"$X=$",
    ha="right",
    va="top",
    fontsize=14,
    fontweight="bold"
)

ax.text(
    -1.05,
    -8.20,
    r"$Y=$",
    ha="right",
    va="top",
    fontsize=14,
    fontweight="bold"
)

# ---------------------------------------------------------
# Axis settings
# ---------------------------------------------------------
ax.set_ylabel(
    "Energy (eV)",
    fontsize=14,
    fontweight="bold"
)

ax.set_ylim(-7.0, 0.5)
ax.set_xlim(-1.5, (len(HOMO)-1)*spacing + 1.5)

# No x-axis ticks
ax.set_xticks([])

# ---------------------------------------------------------
# Spines
# ---------------------------------------------------------
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)

# ---------------------------------------------------------
# Y-axis tick labels - BOLD
# ---------------------------------------------------------
ax.tick_params(
    axis="y",
    labelsize=11,
    width=1.2
)

# Explicitly make Y-axis numbers bold
for label in ax.get_yticklabels():
    label.set_fontweight("bold")
    label.set_fontname("Times New Roman")

# ---------------------------------------------------------
# Legend
# ---------------------------------------------------------
legend = ax.legend(
    loc="upper right",
    fontsize=12,
    frameon=True
)

# Make legend text bold
for text in legend.get_texts():
    text.set_fontweight("bold")
    text.set_fontname("Times New Roman")

# ---------------------------------------------------------
# Layout
# ---------------------------------------------------------
plt.subplots_adjust(
    left=0.08,
    right=0.98,
    top=0.95,
    bottom=0.20
)

# ---------------------------------------------------------
# Display
# ---------------------------------------------------------
plt.show()