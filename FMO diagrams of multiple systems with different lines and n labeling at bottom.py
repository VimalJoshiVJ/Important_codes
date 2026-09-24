import matplotlib.pyplot as plt
import matplotlib as mpl

# =========================================================
# FONT SETTINGS
# =========================================================
mpl.rcParams["font.family"] = "Times New Roman"
mpl.rcParams["font.serif"] = ["Times New Roman"]

mpl.rcParams["font.weight"] = "bold"
mpl.rcParams["axes.labelweight"] = "bold"
mpl.rcParams["axes.titleweight"] = "bold"


# =========================================================
# HOMO AND LUMO DATA
# =========================================================
HOMO = [
    -5.611,
    -5.485,
    -6.132,
    -5.068,
    -5.631,
    -5.394,
    -6.472,
    -4.742,
    -5.807
]

LUMO = [
    -1.608,
    -1.659,
    -2.736,
    -1.469,
    -2.544,
    -1.923,
    -3.722,
    -1.562,
    -3.318
]


# =========================================================
# HOMO-LUMO GAPS
# =========================================================
gaps = [LUMO[i] - HOMO[i] for i in range(len(HOMO))]


# =========================================================
# X AND Y SUBSTITUENTS
# =========================================================
X_labels = [
    "-H",
    "-OH",
    "-OH",
    r"-NH$_2$",
    r"-NH$_2$",
    "-OH",
    "-OH",
    r"-NH$_2$",
    r"-NH$_2$"
]

Y_labels = [
    "-H",
    "-F",
    "-CN",
    "-F",
    "-CN",
    "-F",
    "-CN",
    "-F",
    "-CN"
]


# =========================================================
# FIGURE
# =========================================================
fig, ax = plt.subplots(figsize=(15, 7))

spacing = 3.0


# =========================================================
# ENERGY LEVELS AND GAP ARROWS
# =========================================================
for i in range(len(HOMO)):

    x = i * spacing

    # -----------------------------------------------------
    # HOMO
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
    # LUMO
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
    # HOMO-LUMO GAP ARROWS
    # -----------------------------------------------------

    # First structure: BLACK dotted arrow
    if i == 0:

        ax.annotate(
            "",
            xy=(x, LUMO[i] - 0.03),
            xytext=(x, HOMO[i] + 0.03),
            arrowprops=dict(
                arrowstyle="<->",
                linewidth=1.6,
                color="black",
                linestyle=":"
            )
        )

    # Structures 2-5: BLACK solid arrows
    elif i < 5:

        ax.annotate(
            "",
            xy=(x, LUMO[i] - 0.03),
            xytext=(x, HOMO[i] + 0.03),
            arrowprops=dict(
                arrowstyle="<->",
                linewidth=1.3,
                color="black",
                linestyle="-"
            )
        )

    # Structures 6-9: BLACK dashed arrows
    else:

        ax.annotate(
            "",
            xy=(x, LUMO[i] - 0.03),
            xytext=(x, HOMO[i] + 0.03),
            arrowprops=dict(
                arrowstyle="<->",
                linewidth=1.3,
                color="black",
                linestyle="--"
            )
        )

    # -----------------------------------------------------
    # GAP VALUE
    # -----------------------------------------------------
    ax.text(
        x + 0.15,
        (HOMO[i] + LUMO[i]) / 2,
        f"{gaps[i]:.2f}",
        fontsize=12,
        fontweight="bold",
        va="center",
        ha="left",
        color="black",
        fontname="Times New Roman"
    )


# =========================================================
# X AND Y LABEL ROW POSITIONS
# =========================================================
x_row_y = -0.055
y_row_y = -0.105


# =========================================================
# X= LABEL
# =========================================================
ax.text(
    -0.7,
    x_row_y,
    r"$X=$",
    transform=ax.get_xaxis_transform(),
    ha="right",
    va="top",
    fontsize=14,
    fontweight="bold",
    fontname="Times New Roman"
)


# =========================================================
# Y= LABEL
# =========================================================
ax.text(
    -0.7,
    y_row_y,
    r"$Y=$",
    transform=ax.get_xaxis_transform(),
    ha="right",
    va="top",
    fontsize=14,
    fontweight="bold",
    fontname="Times New Roman"
)


# =========================================================
# X SUBSTITUENT LABELS
# =========================================================
for i in range(len(X_labels)):

    x = i * spacing

    ax.text(
        x,
        x_row_y,
        X_labels[i],
        transform=ax.get_xaxis_transform(),
        ha="center",
        va="top",
        fontsize=14,
        fontweight="bold",
        fontname="Times New Roman"
    )


# =========================================================
# Y SUBSTITUENT LABELS
# =========================================================
for i in range(len(Y_labels)):

    x = i * spacing

    ax.text(
        x,
        y_row_y,
        Y_labels[i],
        transform=ax.get_xaxis_transform(),
        ha="center",
        va="top",
        fontsize=14,
        fontweight="bold",
        fontname="Times New Roman"
    )


# =========================================================
# GROUPING ROW
# =========================================================

# ---------------------------------------------------------
# n = 6 BELOW FIRST -H
# NO ARROW
# ---------------------------------------------------------
ax.text(
    0,
    -0.21,
    r"$n=6$",
    transform=ax.get_xaxis_transform(),
    ha="center",
    va="top",
    fontsize=15,
    fontweight="bold",
    fontname="Times New Roman"
)


# ---------------------------------------------------------
# n = 3 ARROW
# STRUCTURES 2-5
# ---------------------------------------------------------
x_start_n3 = 1 * spacing - 0.65
x_end_n3 = 4 * spacing + 0.65

ax.annotate(
    "",
    xy=(x_end_n3, -0.21),
    xytext=(x_start_n3, -0.21),
    xycoords=ax.get_xaxis_transform(),
    arrowprops=dict(
        arrowstyle="<->",
        linewidth=1.5,
        color="black"
    )
)


# ---------------------------------------------------------
# n = 3 LABEL
# ---------------------------------------------------------
ax.text(
    (x_start_n3 + x_end_n3) / 2,
    -0.21,
    r"$n=3$",
    transform=ax.get_xaxis_transform(),
    ha="center",
    va="center",
    fontsize=15,
    fontweight="bold",
    fontname="Times New Roman",
    bbox=dict(
        facecolor="white",
        edgecolor="none",
        pad=2.0
    )
)


# ---------------------------------------------------------
# n = 6 ARROW
# STRUCTURES 6-9
# ---------------------------------------------------------
x_start_n6 = 5 * spacing - 0.65
x_end_n6 = 8 * spacing + 0.65

ax.annotate(
    "",
    xy=(x_end_n6, -0.21),
    xytext=(x_start_n6, -0.21),
    xycoords=ax.get_xaxis_transform(),
    arrowprops=dict(
        arrowstyle="<->",
        linewidth=1.5,
        color="black"
    )
)


# ---------------------------------------------------------
# n = 6 LABEL
# ---------------------------------------------------------
ax.text(
    (x_start_n6 + x_end_n6) / 2,
    -0.21,
    r"$n=6$",
    transform=ax.get_xaxis_transform(),
    ha="center",
    va="center",
    fontsize=15,
    fontweight="bold",
    fontname="Times New Roman",
    bbox=dict(
        facecolor="white",
        edgecolor="none",
        pad=2.0
    )
)


# =========================================================
# Y-AXIS LABEL
# =========================================================
ax.set_ylabel(
    "Energy (eV)",
    fontsize=14,
    fontweight="bold",
    fontname="Times New Roman"
)


# =========================================================
# AXIS LIMITS
# =========================================================
ax.set_ylim(-7.0, 0.5)

ax.set_xlim(
    -1.5,
    (len(HOMO) - 1) * spacing + 1.5
)


# =========================================================
# REMOVE X-AXIS TICKS
# =========================================================
ax.set_xticks([])


# =========================================================
# REMOVE UNNECESSARY SPINES
# =========================================================
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)


# =========================================================
# Y-AXIS TICKS
# =========================================================
ax.tick_params(
    axis="y",
    labelsize=11,
    width=1.2
)

for label in ax.get_yticklabels():
    label.set_fontweight("bold")
    label.set_fontname("Times New Roman")


# =========================================================
# LEGEND
# =========================================================
legend = ax.legend(
    loc="upper right",
    fontsize=12,
    frameon=True
)

for text in legend.get_texts():
    text.set_fontweight("bold")
    text.set_fontname("Times New Roman")


# =========================================================
# LAYOUT
# =========================================================
plt.subplots_adjust(
    left=0.08,
    right=0.98,
    top=0.95,
    bottom=0.34
)


# =========================================================
# SHOW FIGURE
# =========================================================
plt.show()